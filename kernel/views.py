import datetime
import os.path

from. import my_alipay

from urllib.parse import parse_qs
import alipay
from . import pays
from django.core import serializers
from django.db.models import Min, Count, Max
from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

from django.http import JsonResponse, HttpResponse
import json
import time

import background.models
import login.views
from . import forms
from background.models import Flight,Order,Concrete_flight,FlightSeatingChart
from login.models import User
from .pays import *

# from login.views import response


response = {}
response = login.views.response

@csrf_exempt
def query_flight(request):
    message = '请输入航班信息'

    if request.method == 'POST':

        query_flight_form = forms.QueryFlightForm(request.POST)
        message = '您输入的路线暂无航班直飞，请重新输入'
        # print(query_flight_form)

        if query_flight_form.is_valid():

            origination = query_flight_form.cleaned_data.get('origination')
            destination = query_flight_form.cleaned_data.get('destination')
            date_str = query_flight_form.cleaned_data.get('date')

            year, mouth, day = map(int, date_str.split('-'))
            the_date = datetime.date(year, mouth, day)



            datetime_begin = datetime.datetime(
                the_date.year,the_date.month,the_date.day
                ,0,0,0
            )
            oneday = datetime.timedelta(days=11)
            datetime_end  = datetime.datetime(
                the_date.year, the_date.month, the_date.day
                , 23, 59, 59
            )
            concrete_flight_set = Concrete_flight.objects.filter(flight_datetime__gte=datetime_begin,flight_datetime__lte=datetime_end)


            flight_set = Flight.objects.filter(origination=origination,destination=destination)
            flight_number_set = []
            for flight in flight_set:
                flight_number_set.append(flight.flight_number)
            response['flight_set'] = json.loads(serializers.serialize("json",flight_set))
            response['concrete_flight_set'] = json.loads(serializers.serialize("json",concrete_flight_set))

            flight_list = []

            for concrete_flight in concrete_flight_set:
                if  concrete_flight.flight.flight_number in flight_number_set:

                    my_dict = {}
                    my_dict['flight_time'] = str(concrete_flight.flight.flight_time)
                    my_dict['starting_time'] =str(concrete_flight.flight.starting_time)
                    my_dict['arrival_time'] =str(concrete_flight.flight.arrival_time)
                    my_dict['departure_airport'] =concrete_flight.flight.departure_airport
                    my_dict['landing_airport'] =concrete_flight.flight.landing_airport
                    my_dict['first_class_price'] =concrete_flight.flight.first_class_price
                    my_dict['business_class_price'] =concrete_flight.flight.business_class_price
                    my_dict['economy_class_price'] =concrete_flight.flight.economy_class_price
                    my_dict['flight_number'] =concrete_flight.flight.flight_number
                    my_dict['concrete_flight_id'] = concrete_flight.id
                    my_dict['origination'] = concrete_flight.flight.origination
                    my_dict['destination'] = concrete_flight.flight.destination
                    my_dict['date'] = date_str
                    flight_list.append(my_dict)

            if flight_list.__len__() == 0:
                response['status'] = 1
                response['msg'] = '当日无航班直飞，请选择其他日期'
                print(locals())
                return JsonResponse(response)


            response['flight_list'] = json.dumps(flight_list,ensure_ascii=False)

            response['status'] = 0
            response['msg'] = '查找成功'
            print(locals())
            return JsonResponse(response)
            # flight_list 返回的航班，可以直接输出

            # return render(request, 'list_employee.html', locals())
            # return JsonResponse({
            #     'message':'success'
            # })
        else:
            response['msg'] = message = '你输入的信息无效，请重输入'
            response['status'] = 2

            return JsonResponse(response)
            # return JsonResponse(json.dumps(locals()))
        # return render(request,'list_employee.html',locals())

        # flight_list = Flight.objects.filter(origination='北京')
    # paginator = Paginator(flight_list,3)
    # p=1 分页使用，传送pages
    # try:
    #     pages = paginator.page(p)
    # except PageNotAnInteger:
    #     pages = paginator.page(1)
    # except EmptyPage:
    #     pages = paginator.page(paginator.num_pages)

    # columns = [col[0] for col in flight]
    # print(model_to_dict(flight))
    print(locals())
    # return JsonResponse({'message':'get'})
    return render(request,'list_employee.html',locals())
# @csrf_exempt
# def query_order(request):

@csrf_exempt
def book_ticket(request):


    # if not request.session.get('is_login', None):
    #
    #     response['msg'] = message = '您尚未登录'
    #     response['status'] = -1
    #     return redirect('/login/')
    if request.method == 'POST':
        # username = request.session.get('user_name')
            # return render(request, 'book_ticket.html', locals())
        book_ticket_form = forms.BookTicketForm(request.POST)
        if book_ticket_form.is_valid():
            money = float(book_ticket_form.cleaned_data.get('money'))
            # money = float(request.POST.get('money'))
            flight_number = book_ticket_form.cleaned_data.get('flight_number')
            date_str = book_ticket_form.cleaned_data.get('date')
            Id_number =  book_ticket_form.cleaned_data.get('Id_number')
            real_name =  book_ticket_form.cleaned_data.get('real_name')
            print(date_str)
            year,mouth,day = map(int,date_str.split('-'))
            date = datetime.date(year,mouth,day)
            try:
                user = User.objects.get(Id_number=Id_number)
            except User.DoesNotExist:
                response['msg'] = message = '用户不存在'
                response['status'] = 13
                return JsonResponse(response)
            user_dict = model_to_dict(user)
            response['user'] = user_dict
            if not setting_credit(user):  # 函数在下面
                response['msg'] = message = '您的信用等级较低，无法订票'
                response['status'] = 1
                return JsonResponse(response)

            print(money,flight_number,date)
            try:

                flight = Flight.objects.get(flight_number = flight_number)
                response['flight'] = model_to_dict(flight)
                the_datetime = datetime.datetime(
                    date.year,date.month,date.day,
                    flight.starting_time.hour,flight.starting_time.minute,flight.starting_time.second
                )

                print(the_datetime)
                # the_datetime.date = date
                # the_datetime.time = flight.flight_time
                concrete_flight = Concrete_flight.objects.get(flight=flight,flight_datetime=the_datetime)
                response['concrete_flight'] = model_to_dict(concrete_flight  )
                response['the_datetime'] = the_datetime

                # 同一个人不能买一个机票两次
                try:
                    user = User.objects.get(Id_number = Id_number)
                    order = Order.objects.get(user=user,flight_datetime=the_datetime,order_is_valid=True)
                    response['msg'] = message = '您已经预订过本次航班，请勿重复订购'
                    response['order'] = model_to_dict(order)
                    response['status'] = 2
                    return JsonResponse(response)
                    # return render(request, 'book_ticket.html', locals())
                except User.DoesNotExist:
                    response['msg'] = message = '系统中无此身份证号，请检查输入'
                    response['status'] = 8
                    return JsonResponse(response)
                except Exception as e:
                    pass
                    # 找不到订单就对了
                if user.real_name != real_name:
                    response['msg'] = message = '身份证号姓名与输入姓名不匹配，请重新输入'
                    response['status'] = 7
                    return JsonResponse(response)

                if concrete_flight.book_sum >= concrete_flight.plane_capacity :
                    response['status'] = 3
                    response['msg'] = message = '航班已满，请乘坐其他航班'
                    return JsonResponse(response)
                    # return render(request, 'book_ticket.html', locals())



                # 所以这里使用函数来支付，因为当上面选择支付宝支付的时候也是成功支付了
                print(concrete_flight)
                this_order = pay_ticket(user, flight, date, money)
                print('after')
                response['seat_number'] = this_order.seat_number
                response['msg'] = message = '支付成功'
                response['status'] = 0
                print(message)
                return JsonResponse(response)
                # return render(request, 'book_ticket.html', locals())

            except Flight.DoesNotExist:
                response['msg'] = message = '航班不存在，请重新选择航班'
                response['status'] = 6
                return JsonResponse(response)
                # return render(request, 'book_ticket.html', locals())
            except Concrete_flight.DoesNotExist:
                response['status'] = 5
                response['msg'] = message = '当天该航班并不直飞，请选择其他航班'
                # return render(request, 'book_ticket.html', locals())
                return JsonResponse(response)
        else :
            response['status'] = 7
            response['msg'] = message = '输入信息失效'
    else:
        return render(request,'book_ticket.html',locals())

@csrf_exempt
def cancel_ticket(request):

#
#         return redirect('/login/')
#     username = response['username']

    # username = request.session['user_name']

    if request.method == 'POST':


        #Done 传入订单号
        cancel_form = forms.cancel_ticket_form(request.POST)
        if cancel_form.is_valid():

            order_number = cancel_form.cleaned_data.get('order_number')
            # order_number = request.POST.get('order_number')
            print(order_number)
            order = Order.objects.get(order_number=order_number)
            # username = request.session.get('user_name')
            username = cancel_form.cleaned_data.get('username')
            user = User.objects.get(name=username)
            response['token'] = user.name + user.password
            user = User.objects.get(name=username)
            user_dict = model_to_dict(user)


            try:
                # flight = Flight.objects.get(flight_number=flight_number)
                flight=order.flight
                the_datetime = order.flight_datetime
                # the_datetime = datetime.datetime(
                #     date.year, date.month, date.day,
                #     flight.flight_time.hour, flight.flight_time.minute, flight.flight_time.second
                # )
                concrete_flight = Concrete_flight.objects.get(flight=flight,flight_datetime=the_datetime)

                # return render(request, 'cancel_ticket.html', locals())
                order = Order.objects.get(flight=flight,flight_datetime=concrete_flight.flight_datetime,user=user,order_is_valid=True)

                order.order_is_valid = False
                concrete_flight.book_sum -= 1
                # flight.book_sum -= 1
                user.balance += order.price
                user.total_consumption -= order.price
                #座位设置成False
                seat = FlightSeatingChart.objects.get(concrete_flight=concrete_flight,seat_number=order.seat_number,is_occupied=True)
                seat.is_occupied = False


                setting_credit(user) # 更新信用
                user.save()
                concrete_flight.save()
                order.concrete_flight = concrete_flight
                order.save()
                seat.save()

                response['msg'] = message = '退票成功'
                return JsonResponse(response)
            # return render(request, 'cancel_ticket.html', locals())


            except Flight.DoesNotExist:# 航班不存在
                response['msg'] = message = '航班不存在， 请重新输入'
                return JsonResponse(response)
                # return render(request, 'cancel_ticket.html', locals())
            except Order.DoesNotExist:
                response['msg'] = message = '订单不存在，请重新输入'
                return JsonResponse(response)
                # return render(request, 'cancel_ticket.html', locals())
            except Concrete_flight.DoesNotExist:
                response['msg'] = message = '当天该航班并不直飞，请重新输入'
                return JsonResponse(response)
                # return render(request, 'cancel_ticket.html', locals())
        else :
            response['msg'] = message = '退票失败，格式错误'
            return JsonResponse(response)
            # return JsonResponse({})
    else:
        # return redirect('index/')
        return render(request, 'cancel_ticket.html', locals())
# 计划应该是前端传过来必定有的订单来退订，所以不必设置无法退订不存在的订单

    # 前端传来航班号和购买机票的航班类型
    # 目前采用html输入航班号和类型来实现。。

         # 航班信息不符合，按道理应该是不存在的

def pay_ticket(user,flight,date,money,luggage_weight = 0,seatNumber=-1):
    # pay_type = False : 使用余额支付， 否则支付宝支付 余额支付需要扣除用户余额
    # 还是取消这个设置了，打算用支付宝实现充值就可以了，
    # 这样做反而更麻烦了：加上pay_type对使用支付宝还是余额支付。再说倒也可以
    # seatNumber 默认是-1 如果传进来参数就是自己选座，否则自动分配座位
    response = login.views.response
    contrete_time = datetime.datetime(
        date.year, date.month, date.day,
        flight.starting_time.hour, flight.starting_time.minute, flight.starting_time.second
    )
    # contrete_time.date = date
    # contrete_time.time = flight.flight_time
    print(contrete_time)
    contrete_flight = Concrete_flight.objects.get(flight_datetime=contrete_time,flight=flight)
    print(contrete_flight,1)
    contrete_flight.book_sum += 1
    # flight.book_sum += 1 # 修改
    order = background.models.Order()
    # order.seat_number = flight.book_sum
    # 选座
    new_seat = FlightSeatingChart()
    if seatNumber == -1:
        seat_num = 0
        try:
            for seat_num in range(flight.plane_capacity):
                print(seat_num)
                min_spare_seat_object = FlightSeatingChart.objects.get(is_occupied=True,concrete_flight=contrete_flight,seat_number=int(seat_num)+1)
                print(min_spare_seat_object)
                if min_spare_seat_object is None:
                    min_spare_seat = seat_num+1
                    break


            print('in try')

        except:

            min_spare_seat = seat_num + 1
            # max_occupied_seat_dict = FlightSeatingChart.objects.filter(is_occupied=True,concrete_flight=contrete_flight).aggregate(Max('seat_number'))
            # if max_occupied_seat_dict.get('seat_number__max') is None:
            #     max_occupied_seat = int(0)
            # max_occupied_seat = int(max_occupied_seat_dict.get('seat_number__max'))
            print('in except')
    else:
        min_spare_seat = seatNumber
        # min_spare_seat = max_occupied_seat + 1
    print('seat', min_spare_seat)
    order.seat_number = int(min_spare_seat)
    # 保存新座位
    new_seat.seat_number = min_spare_seat
    new_seat.is_occupied = True
    new_seat.concrete_flight = contrete_flight
    new_seat.save()
    # order.seat_number = contrete_flight.book_sum
    # 有问题，如果有人中途退票了就不能这么放了可能会出现相同的座位号, 于是改成了表的形式
    order.user = user 
    order.flight = flight
    order.order_time = datetime.datetime.now()
    order.flight_datetime = contrete_time
    order.flight_type = get_flight_type(money,flight)

    order.order_is_valid = True
    order.luggage_weight = luggage_weight

    if luggage_weight >20:
        money += 18 *(luggage_weight-20)# 亲测大兴机场价格
    money = float(money)
    if user.credit_rating == '5':# AAA等级至尊用户
        money *= 0.75
    elif user.credit_rating == '4':# AA等级还行用户
        money *=0.9
    elif user.credit_rating == '3': #A级普通用户
        money *= 0.99
    order.price = money
    # if pay_type:
    #
    user.balance -= money
    user.total_consumption += money
    user.save()
    # flight.save()
    contrete_flight.save()
    order.concrete_flight = contrete_flight
    order.concrete_flight.save()
    order.save()
    return order

def get_flight_type(money,flight):
    if money == flight.first_class_price:
        return '1'
    elif money == flight.highlevel_economy_class_price:
        return '2'
    elif money == flight.business_class_price:
        return '3'
    elif money == flight.economy_class_price:
        return '4'
    else :
        return '4'# 不可能出现的情况，保险起见默认设置成经济舱。
    # 只要不出bug hhh



@csrf_exempt
def paysView(request):
    if request.method == 'POST':

        print(response)

        pay_form = forms.pay_form(request.POST)
        if pay_form.is_valid():

            username = request.POST.get('username')
            user = User.objects.get(name=username)
            total = int(request.POST.get('money'))
            # order_id = request.POST.get('order_id')
            # get orderid from frontend or generated by time
            # out_trade_no = str(int(time.time()))
        
            this_alipay = my_alipay.AliPay(
                appid="" ,#TODO Replace it with yours
                app_notify_url= "http://127.0.0.1:8000/api/notify/",
                # app_notify_url=None,
                # alipay_public_key_path=os.path.join(BASE_DIR,'kernel/key/public.txt') , # 支付宝公钥
                # app_private_key_path=os.path.join(BASE_DIR,'kernel/key/private.txt'),  # 应用私钥
                # sign_type = "RSA2",  # 加密方式
                # return_url='http://' + request.get_host() + '/#/personal'  # 支付成功后的返回地址，
                return_url =  'http://127.0.0.1:8000/#/personal',
                debug = True
            )

            query_params = this_alipay.direct_pay(
                subject="机票", # can be generated  by yourself
                out_trade_no = str(int(time.time())),
                total_amount = total,
                # return_url='http://' + request.get_host() + '/#/personal'  # 支付成功后的返回地址，

            )
            return_url = 'http://' + request.get_host() + '/#/personal'  # 支付成功后的返回地址，

            url = "https://openapi.alipaydev.com/gateway.do?{}".format(query_params)
            print(url)
            # url = url.replace('pay¬ify','pay&notiy')
            # url = url.replace('RSA2×tamp', 'RSA2&timestamp')
            # print(url)
            response['url'] = url
            response['return_url'] = return_url
            return JsonResponse(response)

            print(total,'none')
            if total:
                out_trade_no = str(int(time.time()))
                # payInfo = dict(price=total, user_id=request.user.id, state='已支付')
                # request.session['payInfo'] = payInfo # 前段传送逐id 和时间
                # request.session['payTime'] = out_trade_no
                user.balance += total
                user.save()
                return_url = 'http://' + request.get_host()+'/#/personal' # 支付成功后的返回地址，

                url = get_pay(out_trade_no, total, return_url)
                # data = request.query_params.dict()
                # signature = data.pop("sign")
                # print(data)
                # print(signatur
                response['url'] = url

                response['return_url'] = return_url
                return JsonResponse(response)
                # return redirect(url)

            else:
                return JsonResponse({'message': '订单金额不正确'})
        else:
            return JsonResponse({'message': '订单格式不正确'})
    else:
        return render(request, 'pay.html', locals())
        # return JsonResponse({'message': '你的请求不是POST'})
        # return redirect('shopper:shopcart')#

def credit_evaluation(user):
    orders = Order.objects.filter(user=user,order_is_valid=False)
    count_broken_promises = int(0)
    for order in orders:
        order_create_time = order.order_time
        if (datetime.datetime.now()-order_create_time).days <= 30:
            count_broken_promises += 1
    if count_broken_promises >= 3:
        return int(1) # 信用C
    elif count_broken_promises<3 and count_broken_promises > 0:
        return int(2) # 信用B
    else:
        if user.total_consumption > 100000:
            return 5 # AAA
        elif user.total_consumption>10000 and user.total_consumption <=100000:
            return 4 # AA
        else:
            return 3 # A

def setting_credit(user):
    # True 可以订票，False 不可订票
    ret = int(credit_evaluation(user))
    # user.credit_rating = (int(ret) + int('0')) # 对应信用
    if ret == 5:
        user.credit_rating = '5'
    elif ret == 4:
        user.credit_rating = '4'
    elif ret == 3:
        user.credit_rating = '3'
    elif ret == 2:
        user.credit_rating = '2'
    elif ret == 1:
        user.credit_rating = '1'
    else:
        user.credit_rating = '3'
    user.save()
    print('credit ',ret)
    if ret > 1:
        return True
    else:
        return False

@csrf_exempt
def update_order(request):
    if request.method == 'POST':
        print('in update')
        body_str = request.body.decode('utf-8')
        post_data = parse_qs(body_str)

        post_dict = {}

        for k,v in post_data.items():
            post_dict[k] = v[0]
        this_alipay =my_alipay.AliPay(
                appid="", #TODO Replace it with yours
                app_notify_url = "http://127.0.0.1:8000/api/notify/",
                return_url =  'http://127.0.0.1:8000/#/personal',
                debug = True
            )

        sign = post_dict.pop('sign',None)

        status = this_alipay.verify(post_dict,sign)

        if status:
            order_id = post_dict.get('out_trade_no')
            print(order_id)
            print('支付成功')
            return HttpResponse("支付成功")
        else:
            print('支付失败')
            return HttpResponse("支付失败")
    print('not a post')
    return HttpResponse('not a post')

@csrf_exempt
def get_date(request):
    if request.method == 'POST':
        date = datetime.date.today()
        response['date'] = date
        return JsonResponse(response)
