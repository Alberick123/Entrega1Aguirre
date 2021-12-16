from django import forms
import datetime

class EstadioForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=40)
    anioFund = forms.DateField(initial=datetime.date.today)
