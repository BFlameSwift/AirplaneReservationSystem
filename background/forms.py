
from django import  forms

class FlightrForm(forms.Form):
    flight_number = forms.CharField(max_length=30,  label="航班号", widget=forms.TextInput(attrs={'class': 'form-control'}))

    plane_type_choices = [
        ('波音', (
            ('1', '747'),
            ('2', '767'),
            ('3', '777'),
        )
         ),
        ('空客', (
            ('4', 'A300'),
            ('5', 'A310'),
            ('6', 'A320'),
            ('7', 'A340'),
        )
         ),
    ]
    # TODO plane type need
    # plane_type = forms.ChoiceField(label='飞机型号', choices=plane_type_choices,widget=forms.Select)
    origination = forms.CharField(max_length=30,label="始发地", widget=forms.TextInput(attrs={'class': 'form-control'}))
    destination = forms.CharField(max_length=30,label="目的地", widget=forms.TextInput(attrs={'class': 'form-control'}))
    starting_time = forms.TimeField(label="始发时间",widget=forms.TimeInput(attrs={'class': 'form-control'}))


    departure_airport = forms.CharField(max_length=64, label="始发机场", widget=forms.TextInput(attrs={'class': 'form-control'}))
    landing_airport = forms.CharField(max_length=64, label="目的机场", widget=forms.TextInput(attrs={'class': 'form-control'}))
    arrival_time = forms.TimeField(label="到达时间",widget=forms.TimeInput(attrs={'class': 'form-control'}))
    first_class_price = forms.FloatField(label="头等舱价格",widget=forms.NumberInput(attrs={'class': 'form-control'}))
    highlevel_economy_class_price =  forms.FloatField(label="高级经济舱价格",widget=forms.NumberInput(attrs={'class': 'form-control'}))
    business_class_price =  forms.FloatField(label="商务舱价格",widget=forms.NumberInput(attrs={'class': 'form-control'}))
    economy_class_price =  forms.FloatField(label="经济舱价格",widget=forms.NumberInput(attrs={'class': 'form-control'}))


    # book_sum = forms.IntegerField(label="订票总数")
    # plane_capacity = forms.IntegerField(label="飞机容量")
class flight_number_Form(forms.Form):
    flight_number = forms.CharField(max_length=30, label="航班号", widget=forms.TextInput(attrs={'class': 'form-control'}))
