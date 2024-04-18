from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('choice_schedule/<int:id_data_doctor>', views.choice_schedule, name='choice_schedule'),
]