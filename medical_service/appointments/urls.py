from django.urls import path
from .views import add_patients_and_doctors, add_appointments, generate_report, get_today_appointments

urlpatterns = [
    path('add/', add_patients_and_doctors, name='add_patients_and_doctors'),
    path('appointments/add/', add_appointments, name='add_appointments'),
    path('report/', generate_report, name='generate_report'),
    path('appointments/today/', get_today_appointments, name='get_today_appointments'),
]
