# appointments/urls.py

from django.urls import path
from .views import add_patients, add_doctors, add_appointments, report, today_appointments

urlpatterns = [
    path('add_patients/', add_patients, name='add_patients'),
    path('add_doctors/', add_doctors, name='add_doctors'),
    path('add_appointments/', add_appointments, name='add_appointments'),
    path('report/', report, name='report'),
    path('today_appointments/', today_appointments, name='today_appointments'),  # Sử dụng today_appointments
]
