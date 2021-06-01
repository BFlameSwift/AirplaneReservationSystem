import datetime

from django.db.models import Min, Count, Max
from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

from django.http import JsonResponse
import json
import time

import background.models
from . import forms
from background.models import Flight,Order,Concrete_flight,FlightSeatingChart
from login.models import User
from .pays import get_pay


@csrf_exempt
def query_flight(request):
    message = '请输入航班信息'
    response = {}
    if request.method == 'POST':
        print('is post')
        query_flight_form = forms.QueryFlightForm(request.POST)
        message = '您输入的路线暂无航班直飞，请重新输入'
        # print(query_flight_form)

        if query_flight_form.is_valid():
            origination = query_flight_form.cleaned_data.get('origination')
            destination = query_flight_form.cleaned_data.get('destination')
            flight_list = Flight.objects.filter(origination=origination,destination=destination)
            response['flight_list'] = flight_list
            #TODO 可能会有bug
            response['status'] = 1
            print(locals())
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

#TODO 新建订单是如果要预订的机票的飞行时间中已经订过冲突航班了就提示
# 不能同一个人选择同一时间的同一航班 Done
# Done 测试信用评价成功
# TODO 高信用等级打折
    response = {}
    if not request.session.get('is_login', None):

        response['msg'] = message = '您尚未登录'
        response['status'] = -1
        return redirect('/login/')
    if request.method == 'POST':
        username = request.session.get('user_name')
        user = User.objects.get(name=username)
        user_dict = model_to_dict(user)
        response['user'] = user_dict
        if not setting_credit(user): # 函数在下面
            response['msg'] = message = '您的信用等级较低，无法订票'
            response['status'] = 1
            return JsonResponse(response)
            # return render(request, 'book_ticket.html', locals())

        money = float(request.POST.get('money'))
        flight_number = request.POST.get('flight_number')
        date_str = str(request.POST.get('date'))
        year,mouth,day = map(int,date_str.split('-'))
        date = datetime.date(year,mouth,day)


        print(money,flight_number,date)
        try:
            flight = Flight.objects.get(flight_number = flight_number)
            response['flight'] = model_to_dict(flight)
            the_datetime = datetime.datetime(
                date.year,date.month,date.day,
                flight.flight_time.hour,flight.flight_time.minute,flight.flight_time.second
            )
            # the_datetime.date = date
            # the_datetime.time = flight.flight_time
            concrete_flight = Concrete_flight.objects.get(flight=flight,flight_datetime=the_datetime)
            response['concrete_flight'] = model_to_dict(concrete_flight)
            response['the_datetime'] = the_datetime

            # 同一个人不能买一个机票两次
            try:
                order = Order.objects.get(user=user,flight_datetime=the_datetime,order_is_valid=True)
                response['msg'] = message = '您已经预订过本次航班，请勿重复订购'
                response['order'] = model_to_dict(order)
                response['status'] = 2
                return JsonResponse(response)
                # return render(request, 'book_ticket.html', locals())

            except Exception as e:
                pass
                # 找不到订单就对了

            if concrete_flight.book_sum >= concrete_flight.plane_capacity :
                response['status'] = 3
                response['msg'] = message = '航班已满，请乘坐其他航班'
                return JsonResponse(response)
                # return render(request, 'book_ticket.html', locals())

            if user.balance < money:
                # message = '余额不足，请充值，或请您选择是否支付宝付全款'
                response['status'] = 4
                response['msg'] = message = '余额不足，请使用支付宝充值'
                # TODO 选择
                return JsonResponse(response)
                # return render(request, 'book_ticket.html', locals()) # 此时应还有个充值按钮

            # 所以这里使用函数来支付，因为当上面选择支付宝支付的时候也是成功支付了
            pay_ticket(user, flight, date, money)
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

    else:
        return render(request,'book_ticket.html',locals())

@csrf_exempt
def cancel_ticket(request):
# TODO 计划应该是前端传过来必定有的订单来退订，所以不必设置无法退订不存在的订单
    if not request.session.get('is_login', None):
        message = '您尚未登录'

        return redirect('/login/')
    response = {}
    if request.method == 'POST':
        username = request.session.get('user_name')
        user = User.objects.get(name=username)
        user_dict = model_to_dict(user)
        #Done 传入订单号
        order_number = request.POST.get('order_number')
        order = Order.objects.get(order_number=order_number)
        # flight_number = request.POST.get('flight_number')
        # flight_number = order.flight.flight_number
        # date_str = str(request.POST.get('date'))
        # year, mouth, day = map(int, date_str.split('-'))
        # date = datetime.date(year, mouth, day)
        # the_datetime = order.flight_datetime
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

            # TODO 不知道是不是欠考虑了什么
            setting_credit(user) # 更新信用
            user.save()
            concrete_flight.save()
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
    else:
        # return redirect('index/')
        return render(request, 'cancel_ticket.html', locals())
# TODO 计划应该是前端传过来必定有的订单来退订，所以不必设置无法退订不存在的订单

    # 前端传来航班号和购买机票的航班类型
    # 目前采用html输入航班号和类型来实现。。



         # 航班信息不符合，按道理应该是不存在的

def pay_ticket(user,flight,date,money,luggage_weight = 0,seatNumber=-1):
    # pay_type = False : 使用余额支付， 否则支付宝支付 余额支付需要扣除用户余额
    # 还是取消这个设置了，打算用支付宝实现充值就可以了，
    # 这样做反而更麻烦了：加上pay_type对使用支付宝还是余额支付。再说倒也可以
    # seatNumber 默认是-1 如果传进来参数就是自己选座，否则自动分配座位
    contrete_time = datetime.datetime(
        date.year, date.month, date.day,
        flight.flight_time.hour, flight.flight_time.minute, flight.flight_time.second
    )
    # contrete_time.date = date
    # contrete_time.time = flight.flight_time

    contrete_flight = Concrete_flight.objects.get(flight_datetime=contrete_time,flight=flight)
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
                # min_spare_seat = min_spare_seat_dict.get('seat_number__min')
                # if min_spare_seat is None:
                #     min_spare_seat = int(seat_num)
                #     break
            # min_spare_seat_dict = FlightSeatingChart.objects.filter(is_occupied=False,concrete_flight=contrete_flight).aggregate(Min('seat_number'))
            #
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
    # TODO 根据行李重量增加钱，应该至少在get_flight_type 后判断，否则加了钱就不能按照钱来找对应的航班了
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
    #     pass  # TODO 与支付宝对接输入金额
    user.balance -= money
    user.total_consumption += money
    user.save()
    # flight.save()
    contrete_flight.save()
    order.save()

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
        if not request.session.get('is_login', None):
            return redirect('/login/')
        # money_form= moneyForm(request.POST)
        # if money_form.is_valid():
        #     total = money_form.cleaned_data.get('money')
        username = request.session.get('user_name')
        user = User.objects.get(name=username)

        total = int(request.POST.get('money'))
        if total:
            out_trade_no = str(int(time.time()))
            # payInfo = dict(price=total, user_id=request.user.id, state='已支付')
            # request.session['payInfo'] = payInfo # 前段传送逐id 和时间
            # request.session['payTime'] = out_trade_no
            user.balance += total
            user.save()
            return_url = 'http://' + request.get_host() + '.html'# 支付成功后的返回地址，
            url = get_pay(out_trade_no, total, return_url)
            return redirect(url)

        else:
            return JsonResponse({'message': '订单金额不正确'})
    else:
        return render(request, 'pay.html', locals())
        # return JsonResponse({'message': '你的请求不是POST'})
        # return redirect('shopper:shopcart')# TODO ###

def credit_evaluation(user):
    orders = Order.objects.filter(user=user)
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
    if ret > 1:
        return True
    else:
        return False