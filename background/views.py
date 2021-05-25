import datetime
import hashlib

from django.shortcuts import redirect
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from . import forms
from . import models
from .models import Flight
from django.conf import settings
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
            highlevel_economy_class_price = flight_form.cleaned_data.get('highlevel_economy_class_price')
            business_class_price = flight_form.cleaned_data.get('business_class_price')
            economy_class_price = flight_form.cleaned_data.get('economy_class_price')
            plane_type = flight_form.cleaned_data.get('plane_type')

            message = '航班创建成功'
            response = [
                {
                    'status_code':0,
                    'message':message,
                    'flight_number': flight_number,
                    'origination ': origination,
                    'destination': destination,
                    'starting_time': starting_time,
                    'arrival_time': arrival_time,
                    'departure_airport':departure_airport,
                    'landing_airport':landing_airport,
                    'first_class_price':first_class_price,
                    'economy_class_price':economy_class_price,
                },
                {
                    'status_code':1,
                    'message':'已存在相同航班，请先检查历史航班'
                },{
                    'status_code':2,
                    'message':'航班号输入格式有误'
                },{
                    'status_code':3,
                    'message':'该航班舱位价格等级不正确，请检查舱位价格输入，请保证头等舱价格最高、经济舱价格最低'
                },{
                    'status_code':4,
                    'message':'起飞时间晚于降落时间，请检查输入'
                }
            ]

            try:
                same_id_flight = models.Flight.objects.get(flight_number=flight_number)
                message = '已存在相同航班，请先检查历史航班'
                return render(request, 'flight/entry_flight.html', locals())

            except :
                if not check_flight_number(flight_number):
                    message='航班号输入格式有误'
                    return render(request, 'flight/entry_flight.html', locals())
                    # return JsonResponse(response[2])

                if not (first_class_price > highlevel_economy_class_price and highlevel_economy_class_price > business_class_price and business_class_price > economy_class_price):
                    message='该航班舱位价格等级不正确，请检查舱位价格输入，请保证头等舱价格最高、经济舱价格最低'
                    return render(request, 'flight/entry_flight.html', locals())
                    # return JsonResponse(response[3])
                if starting_time > arrival_time:
                    message='起飞时间晚于降落时间，请检查输入'
                    return render(request, 'flight/entry_flight.html', locals())
                    # return JsonResponse(response[4])

                new_flight = models.Flight()
                new_flight.plane_type = plane_type
                new_flight.flight_number = flight_number
                new_flight.origination = origination
                new_flight.destination = destination
                new_flight.starting_time = starting_time
                new_flight.arrival_time = arrival_time
                new_flight.first_class_price = first_class_price
                new_flight.highlevel_economy_class_price = highlevel_economy_class_price
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
                # time_interval = arrival_time.timestamp() - starting_time.timestamp()
                # print('time_interval'+time_interval)
                # print(locals())
                # print(new_flight.flight_time)
                # return render(request,'flight/background.html',locals())
                return render(request, 'flight/entry_flight.html', locals())
        else:
            # TODO 对输入信息逐个处理分别输出相应的错误信息
            message = '请检查输入航班信息是否有效'
            flight_form = forms.FlightrForm()
            return render(request, 'flight/entry_flight.html', locals())
    else:
        flight_form = forms.FlightrForm()
        return render(request, 'flight/entry_flight.html', locals())

@csrf_exempt
def delete_flight(request):
    if request.method == 'POST':
        flight_form = forms.flight_number_Form(request.POST)
        message = '请检查输入的航班号码'
        if flight_form.is_valid():
            flight_num = flight_form.cleaned_data.get('flight_number')
            if not check_flight_number(flight_num):
                message = '航班号格式错误，请重新输入'
                # return JsonResponse({'message': message, 'flight_number': flight_num})
                return render(request, 'flight/delete_flight.html', locals())
            try:
                flight = models.Flight.objects.get(flight_number = flight_num)
                flight.delete()
                message = '航班删除成功'
                return render(request, 'flight/delete_flight.html', locals())
                # return JsonResponse({'message': message, 'flight_number': flight_num})
            except:

                message = '航班不存在，请重新输入'
                print(locals())
                # return JsonResponse({'message':message,'flight_number':flight_num})
                return render(request, 'flight/delete_flight.html', locals())
        else :
            flight_form = forms.flight_number_Form(request.POST)
            # return JsonResponse({'message': message})
            return render(request, 'flight/delete_flight.html', locals())

    else:
        message = '请检查输入航班号码'
        flight_form = forms.flight_number_Form()
        # return JsonResponse({'message': message})
        return render(request, 'flight/delete_flight.html', locals())


def produce_flight_from_date_to_date(flight,start,end):
    start = datetime.date(start)
    end = datetime.date(end)
    days = int(end.day - start.day)
    for i in range(days):
        date = datetime.date
        xday = datetime.timedelta(days=i)
        date = start + xday
        # date.day = date.day+int(i)
        new_flight = models.Concrete_flight()
        new_flight.flight = flight
        new_flight.book_sum = 0
        new_flight.plane_capacity = flight.plane_capacity
        time = flight.flight_time
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

