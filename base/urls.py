from django.urls import path

from . import views

urlpatterns = [
    path('home/',views.home, name = 'home'),
    path('room/', views.home, name='all_rooms')  
]
