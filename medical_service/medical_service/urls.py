# medical_service/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('appointments/', include('appointments.urls')),  # Thêm đường dẫn đến appointments
]
