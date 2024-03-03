from django.urls import path 
from .  import views

#URlconf module
urlpatterns = [
    path('', views.homepage_view),
    path('search/', views.search_view, name='search'),

    ]