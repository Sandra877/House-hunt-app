from django import forms

from .models import register_model

class RegisterForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()

class SubscriptionForm(forms.Form):
    number = forms.CharField(max_length=12,min_length=12)
    amount = forms.IntegerField(min_value=0)

## TO-DO: Encrypt password
class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()
