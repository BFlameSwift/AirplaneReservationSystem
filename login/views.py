import datetime
import hashlib
import re
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict

from . import forms
from .models import *
# from . import
from background.models import *

from django.conf import settings

import json

from django.contrib.auth import authenticate, login

# Create your views here.
response = {}
def hash_code(s, salt='bflame'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()



def index(request): # 个人中心，
    # 向前端传送个人的全部信息和个人的全部订单

    if not request.session.get('is_login',None):
        return redirect('/')

    if request.method == 'POST':
        pass
        # 每一个个人信息都传过来直接保存
    else:
        username = request.session.get('user_name')
        user = User.objects.get(name = username)
        user_dict = model_to_dict(user)
        # 应该可以通过user.''来访问
        # print(json.dumps(user))
        # print(user_value)

        response['user'] = user_dict
        try:
            orders_after = Order.objects.filter(user=user,flight_datetime__gte=datetime.datetime.now()).all()
            orders_before = Order.objects.filter(user=user,flight_datetime__lte=datetime.datetime.now()).all()
            flights_before = {}
            flights_after = {}
            concrete_flights_before = {}
            concrete_flights_after = {}

            show_order_before = []
            show_order_after = []

            # orders_dict = model_to_dict(orders)
            # orders = serializers.serialize('xml',Order.objects.filter(user=user).all(),
            #                                fileds = ('order_number','flight' ,'flight_datetime,','user','price','order_time',
            #                                          'seat_number','order_is_valid','luggage_weight','flight_type'))
            # orders = serializers.serialize('xml', Order.objects.filter(user=user).all(),)
            # 只能打印出来，当然最终应使用第一种查询方法
        except Order.DoesNotExist:
            message = '订单不存在'
            response['msg'] = '订单不存在'
            response['status'] = 1
            # response[]
            return JsonResponse(response)
        # return JsonResponse({'message':message,'user_dict':user_dict})
        except Exception as e:
            # print(flights_after)
            response['status'] = 2
            response['msg'] = str(e)
            return JsonResponse(response)
        i=0
        for order in orders_before:
            flight_dict = model_to_dict(order.flight)
            concrete_flight_dict = model_to_dict(order.concrete_flight)
            flights_before.update({'flight{}'.format(i):flight_dict})
            print('flight{}'.format(i))
            mydict = {}
            mydict['order_id'] = order.order_number
            mydict['flight_number'] = order.flight.flight_number
            mydict['valid'] = order.order_is_valid
            mydict['origination'] = str(order.flight.origination)
            mydict['destination'] = str(order.flight.destination)
            mydict['departure_airport'] = str(order.flight.departure_airport)
            mydict['landing_airport'] = str(order.flight.landing_airport)
            mydict['starting_time'] = order.flight.starting_time.strftime("%H:%M:%S")
            mydict['flight_time'] = order.flight.flight_time.strftime("%H:%M:%S")
            mydict['arrival_time'] = order.flight.arrival_time.strftime("%H:%M:%S")
            mydict['date'] = order.concrete_flight.flight_datetime.strftime('%Y-%m-%d')
            mydict['price'] = order.price
            mydict['flight_type'] = order.flight_type

            show_order_before.append(mydict)

            concrete_flights_before.update({'concrete_flight{}'.format(i):concrete_flight_dict})
            i += 1
        i=0
        for order in orders_after:
            if order.order_is_valid:
                flight_dict = model_to_dict(order.flight)

                concrete_flight_dict = model_to_dict(order.concrete_flight)
                flights_after.update({'flight{}'.format(i): flight_dict})
                print('flight{}'.format(i))
                concrete_flights_before.update({'concrete_flight{}'.format(i): concrete_flight_dict})
                i += 1

                mydict = {}

                mydict['order_id'] = order.order_number
                mydict['flight_number'] = order.flight.flight_number
                mydict['valid'] = order.order_is_valid
                mydict['origination'] = str(order.flight.origination)
                mydict['destination'] = str(order.flight.destination)
                mydict['departure_airport'] = str(order.flight.departure_airport)
                mydict['landing_airport'] = str(order.flight.landing_airport)
                mydict['starting_time'] = order.flight.starting_time.strftime("%H:%M:%S")
                mydict['flight_time'] = order.flight.flight_time.strftime("%H:%M:%S")
                mydict['arrival_time'] = order.flight.arrival_time.strftime("%H:%M:%S")
                mydict['date'] = order.concrete_flight.flight_datetime.strftime('%Y-%m-%d')
                mydict['price'] = order.price
                mydict['flight_type'] = order.flight_type

                show_order_after.append(mydict)

        response['orders_after'] = json.loads(serializers.serialize("json",orders_after))
        response['orders_before'] = json.loads(serializers.serialize("json",orders_before))
        response['flights_after'] = flights_after
        response['flights_before'] = flights_before
        print(show_order_before)

        response['show_order_before'] = json.dumps(show_order_before, ensure_ascii=False)
        response['show_order_after'] = json.dumps(show_order_after, ensure_ascii=False)

        response['concrete_flights_after'] = concrete_flights_after
        response['concrete_flights_before'] = concrete_flights_before


        response['user'] = model_to_dict(user)
        response['status'] = 0
        return JsonResponse(response,safe=False)
        # return HttpResponse(json.dumps(response),content_type="application/json")
    # return JsonResponse(json.dumps({'user':user_dict,'orders':orders},cls=DjangoJSONEncoder),safe=False)
    # return render(request, 'login/index.html')
@csrf_exempt
def  change_information(request):
    if request.method == 'POST':
        information_form = forms.PersonnalInformationForm(request.POST)
        if information_form.is_valid():
            username = information_form.cleaned_data.get('username')
            phone_number = information_form.cleaned_data.get('phone_number')

            sex = information_form.cleaned_data.get('sex')
            birthday_str = information_form.cleaned_data.get('birthday')
            perfession = information_form.cleaned_data.get('perfession')
            year, mouth, day = map(int, birthday_str.split('-'))
            birthday = datetime.date(year, mouth, day)



            old_username = request.session['user_name']

            if username != old_username:
                same_name_user = User.objects.filter(name=username)
                if same_name_user:
                    response['status'] = 4
                    response['msg'] = message = '用户名已经存在'
                    return JsonResponse(response)
            request.session['user_name'] = username

            user = User.objects.get(name=old_username)
            if phone_number != user.phone_number:
                same_phone_number_user = User.objects.filter(phone_number=phone_number)
                if same_phone_number_user:
                    response['status'] = 8
                    response['msg'] = message = '相同的手机号已经存在'
                    return JsonResponse(response)
            user.name = username
            user.phone_number = phone_number
            user.sex = sex
            user.birthday = birthday
            user.perfession = perfession
            user.save()
            response['token'] = user.name + user.password
            response['status'] = 0
            response['msg'] = message = '更改成功'
            return JsonResponse(response)
        else:
            response['msg'] = '输入信息不合法'
            print(information_form)
            response['status'] = 2
            return JsonResponse(response)



# postman 使用x-www-form-urlencoded模式即可
@csrf_exempt
def login(request):

    if request.session.get('is_login', None):  # 不允许重复登录
        username = request.session['user_name']
        user = User.objects.get(name=username)
        response['token'] = user.name+user.password
        # return redirect('/index/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = response['msg'] = '请检查填写的内容！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            # username = request.POST.get('username')
            # password = request.POST.get('password')
            # user = User.objects.get(name=username)


            try:
                user = User.objects.get(name=username)
                # user = User.ob
            except User.DoesNotExist:
                # print(e)
                message = response['msg'] = '用户不存在！'
                response['status'] = 2
                return JsonResponse(response)
                # return render(request, 'login/login.html', locals())
            except Exception as e:
                print(e)
                return JsonResponse(response)
            if not user.has_confirmed:
                response['status'] = 4
                message = response['msg'] = '该用户还未经过邮件确认'
                return JsonResponse(response)
                # return render(request, 'login/login.html', locals())

            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                if user.is_super:
                    response['status'] = 1
                    response['msg'] = '欢迎管理员'+user.name+'!'
                    return JsonResponse(response)

                response['status'] = 0


                token = username+password
                response['token'] = token
                message = response['msg'] = '登录成功'
                # TODO is_super 跳转管理员界面
                return JsonResponse(response)
                # return redirect('/index/')
            else:

                message = response['msg'] = '密码不正确！'
                response['status'] = 3
                return JsonResponse(response)
                # return render(request, 'login/login.html', locals())
        else:
            response['status'] = 5
            return JsonResponse(response)
            # return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()

    return JsonResponse({})
    # return render(request, 'login/login.html', locals())

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
            phone_number = register_form.cleaned_data.get('phone_number')
            birthday = register_form.cleaned_data.get('birthday')
            print(password1,password2)
            print(password1==password2)
            if password1 != password2:
                response['msg'] = message = '两次输入的密码不同！'
                response['status'] = 1
                return JsonResponse(response)
            if not re.match('^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{6,20}$',password1):
                response['msg'] = message = '密码格式错误，请输入8-20位字母+数字密码'
                response['status'] = 7
                return JsonResponse(response)
                # return render(request, 'login/register.html', locals())
            else:
                same_name_user = User.objects.filter(name=username)
                if same_name_user:
                    response['status'] = 2
                    response['msg'] = message = '用户名已经存在'
                    return JsonResponse(response)
                    # return render(request, 'login/register.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:
                    response['status'] = 3
                    response['msg'] = message = '该邮箱已经被注册了！'
                    return JsonResponse(response)
                    # return render(request, 'login/register.html', locals())
                same_id_number_user = User.objects.filter(Id_number = Id_number)
                if same_id_number_user:
                    response['status'] = 4
                    response['msg'] = message = '相同的身份证号已经存在'
                    return JsonResponse(response)
                same_phone_number_user= User.objects.filter(phone_number=phone_number)
                if same_phone_number_user:
                    response['status'] = 8
                    response['msg'] = message = '相同的手机号已经存在'
                    return JsonResponse(response)
                    # return render(request, 'login/register.html', locals())
                new_user = User()

                try:
                    year,mouth,day = map(int,birthday.split('-'))
                    the_date = datetime.date(year,mouth,day)
                    new_user.birthday = the_date
                except:
                    response['status'] = 6
                    response['msg'] = message = '日期格式错误，请按照2021-01-01输入'
                    return JsonResponse(response)

                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.Id_number = Id_number
                new_user.credit_rating = '2'
                new_user.real_name = real_name
                new_user.phone_number = phone_number
                new_user.save()

                code = make_confirm_string(new_user)
                send_email(email, code)
                response['status'] = 0
                response['msg'] = message = '请前往邮箱进行确认！'
                return JsonResponse(response)
                # return render(request, 'login/confirm.html', locals())
        else:
            response['status'] = 5
            response['msg'] = message = '输入格式有误，请检查输入'
            return JsonResponse(response)
            # return render(request, 'login/register.html', locals())
    register_form = forms.RegisterForm()
    return JsonResponse(response)
    # return render(request, 'login/register.html', locals())
@csrf_exempt
def logout(request):
    # if not request.session.get('is_login', None):
    #     return redirect("/login/")
    request.session.flush()
    response['token'] = ''

    return redirect("/")# 修改为返回主界面
    # return redirect("/login/")

def make_confirm_string(user):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    code = hash_code(user.name, now)
    ConfirmString.objects.create(code=code, user=user,)
    return code
def user_confirm(request):
    code = request.GET.get('code', None)
    message = ''
    try:

        confirm = ConfirmString.objects.get(code=code)
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

    text_content = '''感谢注册www.bflame.site ，这里是飞机订票系统的注册邮件。\
                    如果你看到这条消息，说明你的邮箱服务器不提供HTML链接功能，请联系管理员！'''

    html_content = '''
                    <p>感谢注册<a href="http://{}/confirm/?code={}" target=blank>www.bflame.site</a>，\
                    这里是飞机订票系统的站点，用于软件工程大作业课设！</p>
                    <p>请点击站点链接完成注册确认！</p>
                    <p>此链接有效期为{}天！</p>
                    '''.format('127.0.0.1:8000', code, settings.CONFIRM_DAYS)

    msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_HOST_USER, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()

