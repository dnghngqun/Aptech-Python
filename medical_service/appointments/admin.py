from django.contrib import admin
from .models import Patient, Doctor, Appointment
# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date_of_birth', 'gender', 'address', 'phone_number', 'email')
    search_fields = ('full_name', 'email')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'specialization', 'years_of_experience', 'phone_number', 'email')
    search_fields = ('full_name', 'specialization')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_date', 'reason', 'status')
    list_filter = ('status', 'appointment_date')
    search_fields = ('reason',)