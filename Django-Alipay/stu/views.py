from django.shortcuts import render, redirect
from django.http import JsonResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt # cookie
# from .form import *
from .pays import get_pay
import time
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

class moneyForm(forms.Form):
    money  = forms.FloatField(label="价格",widget=forms.NumberInput(attrs={'class': 'form-control'}))



