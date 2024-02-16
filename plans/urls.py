from django.urls import path 
from . import views

#URlconf module
urlpatterns = [
    path('test/', views.testplan),
    path('planspage/', views.plans_view)

]