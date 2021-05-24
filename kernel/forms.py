from django import  forms

class QueryFlightForm(forms.Form):
    origination = forms.CharField(max_length=30, label="始发地", widget=forms.TextInput(attrs={'class': 'form-control'}))
    destination = forms.CharField(max_length=30, label="目的地", widget=forms.TextInput(attrs={'class': 'form-control'}))

