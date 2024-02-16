from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def testplan(request):
    return render(request, 'planstest.html')

def plans_view(request):
    return render(request, 'plansview.html')
