from django.urls import path 
from . import views

#URlconf module
urlpatterns = [
    path('newuser/', views.register_view),
    path('subscribe/', views.subscription_view,name="subscribe"),
    path('login/', views.login_view)

]