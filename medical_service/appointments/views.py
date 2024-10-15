from django.shortcuts import render
from .models import Patient, Doctor, Appointment
from django.http import HttpResponse
import datetime


def add_patients_and_doctors(request):
    if request.method == 'POST':
        # Thêm bệnh nhân
        for i in range(3):
            Patient.objects.create(
                full_name=request.POST.get(f'patient_name_{i+1}'),
                date_of_birth=request.POST.get(f'patient_dob_{i+1}'),
                gender=request.POST.get(f'patient_gender_{i+1}'),
                address=request.POST.get(f'patient_address_{i+1}'),
                phone_number=request.POST.get(f'patient_phone_{i+1}'),
                email=request.POST.get(f'patient_email_{i+1}')
            )
        
        # Thêm bác sĩ
        for i in range(5):
            Doctor.objects.create(
                full_name=request.POST.get(f'doctor_name_{i+1}'),
                specialization=request.POST.get(f'doctor_specialization_{i+1}'),
                phone_number=request.POST.get(f'doctor_phone_{i+1}'),
                email=request.POST.get(f'doctor_email_{i+1}'),
                years_of_experience=request.POST.get(f'doctor_experience_{i+1}')
            )
        return HttpResponse('Đã thêm bệnh nhân và bác sĩ thành công.')

def add_appointments(request):
    if request.method == 'POST':
        for i in range(3):
            patient_id = request.POST.get(f'appointment_patient_{i+1}')
            doctor_id = request.POST.get(f'appointment_doctor_{i+1}')
            appointment_date = request.POST.get(f'appointment_date_{i+1}')
            reason = request.POST.get(f'appointment_reason_{i+1}')
            Appointment.objects.create(
                patient_id=patient_id,
                doctor_id=doctor_id,
                appointment_date=appointment_date,
                reason=reason
            )
        return HttpResponse('Đã thêm cuộc hẹn thành công.')

def generate_report(request):
    appointments = Appointment.objects.all()
    report_data = []
    for appointment in appointments:
        report_data.append({
            'patient_name': appointment.patient.full_name,
            'dob': appointment.patient.date_of_birth,
            'gender': appointment.patient.gender,
            'address': appointment.patient.address,
            'doctor_name': appointment.doctor.full_name,
            'reason': appointment.reason,
            'date': appointment.appointment_date,
        })
    return render(request, 'report.html', {'report_data': report_data})

def get_today_appointments(request):
    today = datetime.date.today()
    appointments = Appointment.objects.filter(appointment_date__date=today)
    return render(request, 'today_appointments.html', {'appointments': appointments})
