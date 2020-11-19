from django import forms
from .models import Car

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = ['name', 'color', 'car_number', 'reg_city']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'car_number':forms.TextInput(attrs={'class':'form-control'}),
            'reg_city':forms.TextInput(attrs={'class':'form-control'}),
        }
