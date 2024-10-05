"""
URL configuration for task_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('login/', views.login_user, name='login_user'),
    path('register/', views.register_user, name='register_user'), 
    path('edit-task/<str:task_id>/', views.edit_task, name='edit_task'),
    path('delete-task/<str:task_id>/', views.delete_task, name='delete_task'),
    path('add-task/', views.add_task, name='add_task'),
    path('update_task_completion/', views.update_task_completion, name='update_task_completion'),
    path('logout/', views.logout_user, name='logout_user'),
]
