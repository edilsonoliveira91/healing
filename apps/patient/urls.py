from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('choice_schedule/<int:id_data_doctor>', views.choice_schedule, name='choice_schedule'),
    path('schedule_time/<int:id_date_open>', views.schedule_time, name='schedule_time'),
    path('my_consultation/', views.my_consultation, name='my_consultation'),
]