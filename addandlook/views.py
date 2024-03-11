from django.shortcuts import render, redirect
from django import forms
from .models import House


# Create your views here.
def addandlook_view(request):
    houses = House.objects.all()  # Query all House objects
    return render(request, 'addandlook.html', {'houses': houses})

from .forms import HouseForm

def addhouse_view(request):
    if request.method == 'POST':
        form = HouseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the homepage
        else:
            # If form is not valid, handle the errors or return the form with errors
            pass
    else:
        form = HouseForm()
    return render(request, 'addhouse.html', {'form': form})

class HouseFilterForm(forms.Form):
    location = forms.CharField(required=False)
    house_type = forms.CharField(required=False)

def house_search(request):
    houses = House.objects.all()
    filtered_houses = houses

    if request.method == 'GET':
        form = HouseFilterForm(request.GET)
        if form.is_valid():
            location = form.cleaned_data.get('location')
            house_type = form.cleaned_data.get('house_type')
            if location:
                filtered_houses = filtered_houses.filter(live_location__icontains=location)
            if house_type:
                filtered_houses = filtered_houses.filter(house_type__icontains=house_type)

    return render(request, 'filteredhouses.html', {'houses': filtered_houses, 'form': form})

#view to show the location and contact details when you click on the detail button
def house_details(request, house_id):
    house = House.objects.get(pk=house_id)
    context = {
        'house': house
    }
    return render(request, 'contactlocation.html', context)