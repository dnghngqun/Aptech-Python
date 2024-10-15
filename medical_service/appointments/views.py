# appointments/views.py

from django.shortcuts import render, redirect
from .models import Patient, Doctor, Appointment
from django.utils import timezone

def add_patients(request):
    if request.method == "POST":
        for _ in range(3):  # Thêm 3 bệnh nhân
            full_name = request.POST.get("full_name")
            date_of_birth = request.POST.get("date_of_birth")
            gender = request.POST.get("gender")
            address = request.POST.get("address")
            phone_number = request.POST.get("phone_number")
            email = request.POST.get("email")
            patient = Patient(
                full_name=full_name,
                date_of_birth=date_of_birth,
                gender=gender,
                address=address,
                phone_number=phone_number,
                email=email
            )
            patient.save()
        return redirect('add_patients')  # Chuyển hướng đến trang thêm bệnh nhân
    return render(request, 'appointments/add_patients.html')


def add_doctors(request):
    if request.method == "POST":
        for _ in range(5):  # Thêm 5 bác sĩ
            full_name = request.POST.get("full_name")
            specialization = request.POST.get("specialization")
            phone_number = request.POST.get("phone_number")
            email = request.POST.get("email")
            years_of_experience = request.POST.get("years_of_experience")
            doctor = Doctor(
                full_name=full_name,
                specialization=specialization,
                phone_number=phone_number,
                email=email,
                years_of_experience=years_of_experience
            )
            doctor.save()
        return redirect('add_doctors')  # Chuyển hướng đến trang thêm bác sĩ
    return render(request, 'appointments/add_doctors.html')


def add_appointments(request):
    if request.method == "POST":
        for _ in range(3):  # Thêm 3 cuộc hẹn
            patient_id = request.POST.get("patient_id")
            doctor_id = request.POST.get("doctor_id")
            appointment_date = request.POST.get("appointment_date")
            reason = request.POST.get("reason")
            appointment = Appointment(
                patient_id=patient_id,
                doctor_id=doctor_id,
                appointment_date=appointment_date,
                reason=reason
            )
            appointment.save()
        return redirect('add_appointments')  # Chuyển hướng đến trang thêm cuộc hẹn
    return render(request, 'appointments/add_appointments.html')


def report(request):
    appointments = Appointment.objects.select_related('patient', 'doctor').all()
    return render(request, 'appointments/report.html', {'appointments': appointments})

def today_appointments(request):
    today = timezone.now().date()
    today_appointments = Appointment.objects.filter(appointment_date__date=today).select_related('patient', 'doctor')
    return render(request, 'appointments/today_appointments.html', {'today_appointments': today_appointments})
