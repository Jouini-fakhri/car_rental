# car_rental/forms.py
from django import forms
from .models import Car
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'category', 'price', 'return_date', 'car_image']
        widgets = {
            'return_date': forms.DateInput(attrs={'type': 'date'}),
        }

    CATEGORY_CHOICES = [
        ('Normal', 'Normal'),
        ('Luxury', 'Luxury'),
    ]
    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    car_image = forms.ImageField(required=False, widget=forms.FileInput)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CarBrandFilterForm(forms.Form):
    brand = forms.CharField(label='Brand', required=False)