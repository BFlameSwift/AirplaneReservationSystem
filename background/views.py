import datetime
import hashlib

from django.shortcuts import redirect
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from . import forms
from . import models
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
            starting_time = flight_form.cleaned_data.get('starting_time')
            arrival_time = flight_form.cleaned_data.get('arrival_time')
            first_class_price = flight_form.cleaned_data.get('first_class_price')
            highlevel_economy_class_price = flight_form.cleaned_data.get('highlevel_economy_class_price')
            business_class_price = flight_form.cleaned_data.get('business_class_price')
            economy_class_price = flight_form.cleaned_data.get('economy_class_price')

            response = [
                {
                    'status_code': 0,
                    'flight_number': flight_number,
                    'origination ': origination,
                    'destination': destination,
                    'starting_time': starting_time,
                    'arrival_time': arrival_time,

                },

            ]

            try:
                same_id_flight = models.Flight.objects.get(flight_number=flight_number)
                message = '航班已经存在'
                return render(request, 'background/background..html', locals())
            except :

            # TODO 检测航班号是否非法
                new_flight = models.Flight()
                new_flight.flight_number = flight_number
                new_flight.origination = origination
                new_flight.destination = destination
                new_flight.starting_time = starting_time
                new_flight.arrival_time = arrival_time
                new_flight.first_class_price = first_class_price
                new_flight.highlevel_economy_class_price = highlevel_economy_class_price
                new_flight.business_class_price = business_class_price
                new_flight.economy_class_price = economy_class_price
                print(locals())

                return JsonResponse(response[0])
        else:
            print(flight_form)
            return JsonResponse({'message':'error'})

            # interval = arrival_time - starting_time


            # try:
            #     flight = models.Flight.objects.get(name=flight_number)
            # except:
            #     message = '航班不存在'
            #     return render(request,'background/background..html',local())



