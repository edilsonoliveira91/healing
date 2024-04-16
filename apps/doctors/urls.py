from django.urls import path
from . import views

urlpatterns = [
    path('create_doctor/', views.create_doctor, name='create_doctor' ),
]