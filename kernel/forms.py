from django import  forms

class QueryFlightForm(forms.Form):
    origination = forms.CharField(max_length=30, label="始发地", widget=forms.TextInput(attrs={'class': 'form-control'}))
    destination = forms.CharField(max_length=30, label="目的地", widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.CharField(max_length=30, label="目的地", widget=forms.TextInput(attrs={'class': 'form-control'}))

class BookTicketForm(forms.Form):
    date = forms.CharField(max_length=30, label="日期", widget=forms.TextInput(attrs={'class': 'form-control'}))

    real_name = forms.CharField(max_length=30, label="真实姓名", widget=forms.TextInput(attrs={'class': 'form-control'}))
    Id_number = forms.CharField(max_length=30, label="身份证号", widget=forms.TextInput(attrs={'class': 'form-control'}))
    flight_number = forms.CharField(max_length=30, label="航班号", widget=forms.TextInput(attrs={'class': 'form-control'}))
    money = forms.FloatField()

class pay_form(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    money = forms.FloatField()
    order_id = forms.IntegerField()

class cancel_ticket_form(forms.Form):
    order_number = forms.CharField(max_length=30, label="日期", widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))