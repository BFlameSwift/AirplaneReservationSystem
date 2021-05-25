import datetime

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
from background.models import Flight,Order
from login.models import User
from .pays import get_pay


@csrf_exempt
def query_flight(request):
    message = '请输入航班信息'
    if request.method == 'POST':
        print('is post')
        query_flight_form = forms.QueryFlightForm(request.POST)
        message = '您输入的路线暂无航班直飞，请重新输入'
        # print(query_flight_form)

        if query_flight_form.is_valid():
            origination = query_flight_form.cleaned_data.get('origination')
            destination = query_flight_form.cleaned_data.get('destination')
            flight_list = Flight.objects.filter(origination=origination,destination=destination)
            print(locals())
            # flight_list 返回的航班，可以直接输出
            return render(request, 'list_employee.html', locals())
            # return JsonResponse({
            #     'message':'success'
            # })
        else:
            message = '你输入的信息无效，请重输入'
            return JsonResponse(json.dumps(locals()))
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

    if not request.session.get('is_login', None):
        message = '您尚未登录'
        return redirect('/login/')
    if request.method == 'POST':
        username = request.session.get('user_name')
        user = User.objects.get(name=username)
        user_dict = model_to_dict(user)

        money = float(request.POST.get('money'))
        flight_number = request.POST.get('flight_number')
        print(money,flight_number)
        try:
            flight = Flight.objects.get(flight_number = flight_number)
            if user.balance < money:
                message = '余额不足，请充值，或请您选择是否支付宝付全款'
                # TODO 选择

                return render(request, 'book_ticket.html', locals()) # 此时应还有个充值按钮
            # 所以这里使用函数来支付，因为当上面选择支付宝支付的时候也是成功支付了
            pay_ticket(user,flight,money)
            message = '支付成功'
            print(message)
            return render(request, 'book_ticket.html', locals())

        except Flight.DoesNotExist:# 航班不存在
            message = '航班不存在， 请重新输入'
            return render(request,'book_ticket.html',locals())


    else:
        return render(request,'book_ticket.html',locals())

@csrf_exempt
def cancel_ticket(request):
    if not request.session.get('is_login', None):
        message = '您尚未登录'
        return redirect('/login/')
    if request.method == 'POST':
        username = request.session.get('user_name')
        user = User.objects.get(name=username)
        user_dict = model_to_dict(user)
        flight_number = request.POST.get('flight_number')
        try:
            flight = Flight.objects.get(flight_number=flight_number)


            # return render(request, 'cancel_ticket.html', locals())
            order = Order.objects.get(flight=flight)

            order.order_is_valid = False
            flight.book_sum -= 1
            user.balance += order.price
            user.total_consumption -= order.price
            # TODO 不知道是不是欠考虑了什么
            
            message = '退票成功'
            return render(request, 'cancel_ticket.html', locals())


        except Flight.DoesNotExist:# 航班不存在
            message = '航班不存在， 请重新输入'
            return render(request, 'cancel_ticket.html', locals())
        except Order.DoesNotExist:
            message = '订单不存在，请重新输入'
            return render(request, 'cancel_ticket.html', locals())


    else:
        return render(request, 'cancel_ticket.html', locals())


    # 前端传来航班号和购买机票的航班类型
    # 目前采用html输入航班号和类型来实现。。



         # 航班信息不符合，按道理应该是不存在的

def pay_ticket(user,flight,money,pay_type = False,luggage_weight = 0):
    # pay_type = False : 使用余额支付， 否则支付宝支付 余额支付需要扣除用户余额


    flight.book_sum += 1
    order = background.models.Order()
    order.seat_number = flight.book_sum
    order.user = user
    order.flight = flight
    order.order_time = datetime.datetime.now()
    order.flight_type = get_flight_type(money,flight)
    order.price = money
    order.order_is_valid = True
    order.luggage_weight = luggage_weight
    # TODO 根据行李重量增加钱，应该至少在get_flight_type 后判断，否则加了钱就不能按照钱来找对应的航班了
    if luggage_weight >20:
        money += 18 *(luggage_weight-20)

    if not pay_type:
        user.balance -= float(money)

    if pay_type:
        pass  # TODO 与支付宝对接输入金额

    user.total_consumption += money
    user.save()
    flight.save()
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
        return '4'




@csrf_exempt
def paysView(request):
    if request.method == 'POST':
        # money_form= moneyForm(request.POST)
        # if money_form.is_valid():
        #     total = money_form.cleaned_data.get('money')
        total = int(request.POST.get('money'))
        if total:
            out_trade_no = str(int(time.time()))
            # payInfo = dict(price=total, user_id=request.user.id, state='已支付')
            # request.session['payInfo'] = payInfo # 前段传送逐id 和时间
            # request.session['payTime'] = out_trade_no

            return_url = 'http://' + request.get_host() + '/shopper.html'# 支付成功后的返回地址，
            url = get_pay(out_trade_no, total, return_url)
            return redirect(url)

        else:
            return JsonResponse({'message': '订单金额不正确'})
    else:
        return render(request, 'book_ticket.html', locals())
        # return JsonResponse({'message': '你的请求不是POST'})
        # return redirect('shopper:shopcart')# TODO ###