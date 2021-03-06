import datetime
import hashlib
import json
from django.shortcuts import redirect
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from . import forms
from . import models
from .models import Flight,Concrete_flight
from login.views import response
from django.conf import settings

@csrf_exempt
def show_flight(request):
    if request.method == 'POST':
        flight_list = Flight.objects.all()
        show_flight_list = []
        for flight in flight_list:
            mydict = {}
            mydict['flight_number'] = flight.flight_number
            mydict['origination'] =flight.origination
            mydict['destination'] =flight.destination
            mydict['departure_airport'] = flight.departure_airport
            mydict['landing_airport'] =flight.landing_airport
            mydict['starting_time'] =str(flight.starting_time)
            mydict['flight_time'] =str(flight.flight_time)
            mydict['arrival_time'] =str(flight.arrival_time)
            mydict['first_class_price'] = flight.first_class_price
            mydict['business_class_price'] = flight.business_class_price
            mydict['economy_class_price'] =flight.economy_class_price
            mydict['plane_capacity'] =flight.plane_capacity
            show_flight_list.append(mydict)

        response['show_flight_list'] = json.dumps(show_flight_list, ensure_ascii=False)
        return JsonResponse(response)
    else:
        return JsonResponse({})
@csrf_exempt
def entry_flight(request):
    # if request.session.get('is_login',None):
    #     return redirect('/background/')
    if request.method == 'POST':

        flight_form = forms.FlightrForm(request.POST)
        message = '请检查你的输入内容'
        if flight_form.is_valid():

            flight_number = flight_form.cleaned_data.get('flight_number')
            origination = flight_form.cleaned_data.get('origination')
            destination = flight_form.cleaned_data.get('destination')
            departure_airport = flight_form.cleaned_data.get('departure_airport')
            landing_airport = flight_form.cleaned_data.get('landing_airport')
            starting_time = flight_form.cleaned_data.get('starting_time')
            arrival_time = flight_form.cleaned_data.get('arrival_time')
            first_class_price = flight_form.cleaned_data.get('first_class_price')
            # highlevel_economy_class_price = flight_form.cleaned_data.get('highlevel_economy_class_price')
            business_class_price = flight_form.cleaned_data.get('business_class_price')
            economy_class_price = flight_form.cleaned_data.get('economy_class_price')
            plane_type = flight_form.cleaned_data.get('plane_type')
            start_date_str = flight_form.cleaned_data.get('starting_date')
            end_date_str = flight_form.cleaned_data.get('ending_date')

            start_date_str = str(start_date_str)
            end_date_str = str(end_date_str)
            year1, mouth1, day1 = map(int, start_date_str.split('-'))
            year2, mouth2, day2 = map(int, end_date_str.split('-'))
            start_date = datetime.date(year1, mouth1, day1)
            end_date = datetime.date(year2, mouth2, day2)


            try:
                same_id_flight = models.Flight.objects.get(flight_number=flight_number)
                response['status'] = 1
                response['msg'] = message = '已存在相同航班，请先检查历史航班'
                return JsonResponse(response)
                # return render(request, 'flight/entry_flight.html', locals())

            except :
                if not check_flight_number(flight_number):
                    response['status'] = 2
                    response['msg'] = message = '航班号输入格式有误'
                    return JsonResponse(response)
                    # return render(request, 'flight/entry_flight.html', locals())
                    # return JsonResponse(response[2])

                if not (first_class_price > business_class_price and business_class_price > economy_class_price):
                    response['status'] = 3
                    response['msg'] = message='该航班舱位价格等级不正确，请检查舱位价格输入，请保证头等舱价格最高、经济舱价格最低'
                    return JsonResponse(response)
                    # return render(request, 'flight/entry_flight.html', locals())
                    # return JsonResponse(response[3])
                if starting_time > arrival_time:
                    response['status'] = 4
                    response['msg'] = message = '起飞时间晚于降落时间，请检查输入'
                    # return render(request, 'flight/entry_flight.html', locals())
                    return JsonResponse(response)

                new_flight = models.Flight()
                new_flight.plane_type = plane_type
                new_flight.flight_number = flight_number
                new_flight.origination = origination
                new_flight.destination = destination
                new_flight.starting_time = starting_time
                new_flight.arrival_time = arrival_time
                new_flight.first_class_price = first_class_price
                # new_flight.highlevel_economy_class_price = highlevel_economy_class_price
                new_flight.business_class_price = business_class_price
                new_flight.economy_class_price = economy_class_price
                new_flight.landing_airport = landing_airport
                new_flight.departure_airport = departure_airport
                # new_flight.flight_time = arrival_time - starting_time
                a_time = arrival_time
                s_time = starting_time

                if a_time.minute<s_time.minute:
                    new_flight.flight_time = datetime.time(a_time.hour-1-s_time.hour, a_time.minute+60-s_time.minute)
                else:
                    new_flight.flight_time = datetime.time(a_time.hour - s_time.hour,
                                                           a_time.minute  - s_time.minute)

                # new_flight.flight_time = datetime.time(a_time.hour-s_time.hour,)
                new_flight.book_sum = 0
                new_flight.plane_capacity = setting_plane_capacity(plane_type)
                # new_flight.plane_capacity = 200# 根据飞机型号定制 完成

                new_flight.save()

                try:
                    flight = Flight.objects.get(flight_number=flight_number)
                    produce_flight_from_date_to_date(flight, start_date, end_date)


                except Flight.DoesNotExist:
                    response['msg'] = message = '航班不存在，请重新输入'
                    return render(request, 'produce_flight.html', locals())
                response['status'] = 0
                response['msg'] = '航班创建成功'
                # time_interval = arrival_time.timestamp() - starting_time.timestamp()

                # return render(request,'flight/background.html',locals())
                return JsonResponse(response)
                # return render(request, 'flight/entry_flight.html', locals())
        else:

            response['msg'] = message = '请检查输入航班信息是否有效'
            response['status'] = 5
            # flight_form = forms.FlightrForm()
            print(flight_form)
            return JsonResponse(response)
            # return render(request, 'flight/entry_flight.html', locals())
    else:
        flight_form = forms.FlightrForm()
        return render(request, 'flight/entry_flight.html', locals())

@csrf_exempt
def delete_con_flight(request):
    if request.method == 'POST':
        concrete_form = forms.concrete_flight_id_Form(request.POST)
        if concrete_form.is_valid():
            concrete_id = concrete_form.cleaned_data.get('concrete_flight_id')
            concrete_flight = Concrete_flight.objects.get(id = concrete_id)
            concrete_flight.delete()
            response['status'] = 0
            response['msg'] = 'success'
            return JsonResponse(response)
        else :
            response['status'] = 2
            response['msg'] = '输入错误'
            return JsonResponse(response)

@csrf_exempt
def delete_flight(request):

    if request.method == 'POST':
        flight_form = forms.flight_number_Form(request.POST)

        response['msg'] = message = '请检查输入的航班号码'
        if flight_form.is_valid():
            flight_num = flight_form.cleaned_data.get('flight_number')
            if not check_flight_number(flight_num):
                response['status'] = 2
                response['msg'] = message = '航班号格式错误，请重新输入'
                # return JsonResponse({'message': message, 'flight_number': flight_num})
                return JsonResponse(response)
                # return render(request, 'flight/delete_flight.html', locals())
            try:
                flight = models.Flight.objects.get(flight_number = flight_num)
                flight.delete()
                response['msg'] = message = '航班删除成功'
                response['status'] = 3
                return JsonResponse(response)

                # return render(request, 'flight/delete_flight.html', locals())
                # return JsonResponse({'message': message, 'flight_number': flight_num})
            except:
                response['status'] = 6
                response['msg'] = message = '航班不存在，请重新输入'
                print(locals())
                return JsonResponse(response)
                # return JsonResponse({'message':message,'flight_number':flight_num})
                # return render(request, 'flight/delete_flight.html', locals())
        else :
            flight_form = forms.flight_number_Form(request.POST)
            # return JsonResponse({'message': message})
            response['status'] = 4
            response['msg'] = message = '航班号格式错误'
            return JsonResponse(response)
            # return render(request, 'flight/delete_flight.html', locals())

    else:
        # message = '请检查输入航班号码'
        flight_form = forms.flight_number_Form()
        # return JsonResponse({'message': message})
        return render(request, 'flight/delete_flight.html', locals())


def setting_new_flight(request):
    if request.method == 'POST':
        start_stop_date_form = forms.StartStopDateForm(request.POST)
        if start_stop_date_form.is_valid():
            start_date_str = start_stop_date_form.cleaned_data.get('starting_date')
            end_date_str = start_stop_date_form.cleaned_data.get('ending_date')
            flight_number = start_stop_date_form.cleaned_data.get('flight_number')
            start_date_str = str(start_date_str)
            end_date_str = str(end_date_str)
            year1,mouth1,day1 = map(int, start_date_str.split('-'))
            year2,mouth2,day2 = map(int, end_date_str.split('-'))
            start_date = datetime.date(year1,mouth1,day1)
            end_date =  datetime.date(year2,mouth2,day2)

            try:
                flight = Flight.objects.get(flight_number = flight_number)
                produce_flight_from_date_to_date(flight,start_date,end_date)
                message = '产生航班成功'
                return render(request, 'produce_flight.html', locals())

            except Flight.DoesNotExist:
                message = '航班不存在，请重新输入'
                return render(request, 'produce_flight.html', locals())
            # produce_flight_from_date_to_date()
        else:
            message = '请以2021-01-01的格式输入日期'
            return render(request, 'produce_flight.html', locals())

    else:
        return render(request,'produce_flight.html',locals())


def produce_flight_from_date_to_date(flight,start,end):

    print(start)
    print(end)
    days = (end-start).days
    print(days)
    for i in range(days):

        date = datetime.date
        xday = datetime.timedelta(days=i)
        date = start + xday
        print(date)
        # date.day = date.day+int(i)
        new_flight = models.Concrete_flight()
        new_flight.flight = flight
        new_flight.book_sum = 0
        new_flight.plane_capacity = flight.plane_capacity
        time = flight.starting_time
        # time = datetime.time()
        new_flight.flight_datetime = datetime.datetime(
            year=date.year,month=date.month,day=date.day,
            hour=time.hour,minute=time.minute,second=time.second
        )
        new_flight.save()

    # pass

# 从起始到终止产生相同时间的航班到数据库中。
#从道理来讲，航班也总会有停止运行的时间
# 如果未来设置航班总需要这个东西。为了保证航班号作为逐主键存在于数据库中

def check_flight_number(flight_number):
    flight_number = str(flight_number)
    if not flight_number[0:2].isupper():
        return False

    if not flight_number[2:6].isdigit():
        return False
    return len(flight_number) == 6

def setting_plane_capacity(plane_type):
    num = 200
    # 数据以中国国际航空公司的主要数据为准
    if plane_type == '1':
        num = 365
        # 波音747
    elif plane_type == '2':
        num = 311
        # 波音777
    elif plane_type == '3':
        num = 293
        # 波音787-9
    elif plane_type == '4':
        num = 259
        #空客A300B1
    elif plane_type == '5':
        num = 220
        # 空客310-300
    elif plane_type == '6':
        num = 180
        # 空客320-200
    elif plane_type == '7':
        num = 440
        #空客350-900
    return int(num)

