from django.urls import path
from . import views

urlpatterns = [
    path('create_doctor/', views.create_doctor, name='create_doctor' ),
    path('schedule/', views.schedule, name='schedule'),
    path('medical_appointment/', views.medical_appointment, name='medical_appointment'),
]