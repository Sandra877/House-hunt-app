from django.urls import path 
from .  import views

#URlconf module
urlpatterns = [
    path('main/', views.addandlook_view),
    path('addhouse/', views.addhouse_view, name='addhouse'),
    path('house-search/', views.house_search, name='house_search'),
    path('house_details/<int:house_id>/', views.house_details, name='house_details'),




    ]