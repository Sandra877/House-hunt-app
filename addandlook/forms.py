from django import forms
from .models import House
from django.shortcuts import render


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['image1', 'image2', 'video', 'contact', 'live_location', 'house_type']

