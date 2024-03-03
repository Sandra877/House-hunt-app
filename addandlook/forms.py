from django import forms
from .models import House

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['image1', 'image2', 'video', 'contact', 'live_location']
