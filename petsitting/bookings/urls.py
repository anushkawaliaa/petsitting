from django.urls import path
from . import views

app_name = 'bookings'

urlpatterns = [
    path('', views.home, name='home'),
    path('booking/', views.create_booking, name='create_booking'),
    path('success/', views.success, name='success'),
]
