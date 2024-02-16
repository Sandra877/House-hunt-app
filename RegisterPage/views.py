from django.shortcuts import render,redirect

from .forms import *
from .models import *
from .payment import *
# Create your views here.
def register_view(request):
    my_form = RegisterForm()
    if request.method == "POST":
        my_form = RegisterForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            register_model.objects.create(**my_form.cleaned_data)
            return redirect("subscribe")
        else:
            print(my_form.errors)

    context = {
        "form" : my_form
    
    }
    return render(request, 'registerform.html', context)

def subscription_view(request):
    my_form = SubscriptionForm()
    if request.method == "POST":
        my_form = SubscriptionForm(request.POST)
        if my_form.is_valid():
            number = my_form.cleaned_data["number"]
            amount = my_form.cleaned_data["amount"]
            return render(request, 'response.html', {"data":makepayment(number,amount)})
            
        else:
            print(my_form.errors)

    context = {
        "form" : my_form}
    return render(request, 'subscription.html', context)

def login_view(request):
    my_form = LoginForm()
    if request.method == "POST":
        my_form = LoginForm(request.POST)
        if my_form.is_valid():
            email = my_form.cleaned_data["email"]
            passw = my_form.cleaned_data["password"]

            try:
                user = register_model.objects.get(email=email,password=passw)
                return redirect("subscribe")
            except:
                print("Does not exists")
            
        else:
            print(my_form.errors)

    context = {
        "form" : my_form
    
    }
    return render(request, 'loginform.html', context)
    