import datetime
import hashlib

from django.shortcuts import redirect
from django.shortcuts import render
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict

import background.models
from . import forms
from .models import *
from . import models
from background.models import *

from django.conf import settings

import json

# Create your views here.

def hash_code(s, salt='bflame'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()



def index(request): # 个人中心，
    # 向前端传送个人的全部信息和个人的全部订单
    if not request.session.get('is_login',None):
        return redirect('/login/')
    username = request.session.get('user_name')
    user = User.objects.get(name = username)
    user_dict = model_to_dict(user)
    # 应该可以通过user.''来访问
    # print(json.dumps(user))
    # print(user_value)
    try:
        # orders = Order.objects.filter(user=user).all()
        # orders = serializers.serialize('xml',Order.objects.filter(user=user).all(),
        #                                fileds = ('order_number','flight' ,'flight_datetime,','user','price','order_time',
        #                                          'seat_number','order_is_valid','luggage_weight','flight_type'))
        orders = serializers.serialize('xml', Order.objects.filter(user=user).all(),)
        # 只能打印出来，当然最终应使用第一种查询方法
    except Order.DoesNotExist:
        message = '订单不存在'
        return JsonResponse({'message':message,'user_dict':user_dict})
    # data = serializers.serialize('xml',models.User.objects.all(),fileds = ('name','password'))
    # List = list(flight_list)
    # print(model_to_dict(orders))
    # order = Order()
    # for order in orders:
    #     print(order)
    # print(orders)
    return JsonResponse(json.dumps({'user':user_dict,'orders':orders},cls=DjangoJSONEncoder),safe=False)
    # return render(request, 'login/index.html')

def  change_information(request):
    pass
# TODO 逐个更改个人信息

# postman 使用x-www-form-urlencoded模式即可
@csrf_exempt
def login(request):

    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')

            try:
                user = models.User.objects.get(name=username)
            except :
                message = '用户不存在！'
                # return JsonResponse(response[2])
                return render(request, 'login/login.html', locals())

            if not user.has_confirmed:
                message = '该用户还未经过邮件确认！'
                # return JsonResponse(response[4])
                return render(request, 'login/login.html', locals())

            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                # return JsonResponse(response[0])
                return redirect('/index/')
            else:
                message = '密码不正确！'
                # return JsonResponse(response[3])
                return render(request, 'login/login.html', locals())
        else:
            # return JsonResponse(response[5])
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    # return JsonResponse({})
    return render(request, 'login/login.html', locals())

@csrf_exempt
def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            email = register_form.cleaned_data.get('email')
            sex = register_form.cleaned_data.get('sex')
            Id_number = register_form.cleaned_data.get('Id_number')
            real_name = register_form.cleaned_data.get('real_name')
            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱已经被注册了！'
                    return render(request, 'login/register.html', locals())
                same_id_number_user = models.User.objects.filter(Id_number = Id_number)
                if same_id_number_user:
                    message = '相同的身份证号已经存在'
                    return render(request, 'login/register.html', locals())

                new_user = models.User()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.Id_number = Id_number
                new_user.credit_rating = '2'
                new_user.real_name = real_name
                new_user.save()

                code = make_confirm_string(new_user)
                send_email(email, code)

                message = '请前往邮箱进行确认！'
                return render(request, 'login/confirm.html', locals())
        else:
            return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/login/")
    request.session.flush()
    return redirect("/login/")

def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name, now)
    models.ConfirmString.objects.create(code=code, user=user,)
    return code
def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:
        confirm = models.ConfirmString.objects.get(code=code)
    except:
        message = '无效的确认请求!'
        return render(request, 'login/confirm.html', locals())

    c_time = confirm.c_time
    now = datetime.datetime.now()
    from AirplaneReservationSystem import settings
    if now > c_time + datetime.timedelta(settings.CONFIRM_DAYS):
        confirm.user.delete()
        message = '您的邮件已经过期！请重新注册!'
        return render(request, 'login/confirm.html', locals())
    else:
        confirm.user.has_confirmed = True
        confirm.user.save()
        confirm.delete()
        message = '感谢确认，请使用账户登录！'
        return render(request, 'login/confirm.html', locals())



def send_email(email, code):

    from django.core.mail import EmailMultiAlternatives

    subject = '来自www.bflame.site的注册确认邮件'

    text_content = '''感谢注册www.bflame.site ，这里是李彧的博客和教程站点，专注于摸鱼技术的分享！\
                    如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！'''

    html_content = '''
                    <p>感谢注册<a href="http://{}/confirm/?code={}" target=blank>www.bflame.site</a>，\
                    这里是李彧的博客和教程站点，专注于摸鱼技术的分享！</p>
                    <p>请点击站点链接完成注册确认！</p>
                    <p>此链接有效期为{}天！</p>
                    '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


