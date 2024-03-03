from django.urls import path 
from .  import views

#URlconf module
urlpatterns = [
    path('main/', views.addandlook_view),
    path('addhouse/', views.addhouse_view, name='addhouse'),


    ]