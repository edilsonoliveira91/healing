from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

#IMPORTS MODELS
from doctors.models import DoctorProfile, Skills, Schedule
from .models import Consultation

#IMPORT MESSAGES
from django.contrib import messages
from django.contrib.messages import constants

def home(request):
    if request.method == 'GET':
        print(request.user)
        print()
        doctor_filter = request.GET.get('doctor')
        skill_filter = request.GET.getlist('skill')
        doctors = DoctorProfile.objects.all()

        if doctor_filter:
            # Aqui vamos filtrar no campo para procurar o medico e colando o parametro name__icontains nos iremos trazer do banco de dados todos os nomes que contem o que foi digitado.. se o usuario digitou apenas 2 letras, ira ser procurado nomes que contem aquelas duas letras.
            doctors = doctors.filter(name__icontains=doctor_filter)
        
        if skill_filter:
            # Aqui estamos filtrandos a lista de skill e passamos esse paramentro skill_id__in onde nossa skill é uma foreignkey e sendo uma lista e o usuario podendo selecionar mais de uma skill entao passamos o __in para dizer que queremos filtrar todos os campos selecionados. 
            doctors = doctors.filter(skill_id__in=skill_filter)

        list_skill = Skills.objects.all()
        return render(request, 'home.html', {'doctors': doctors, 'list_skill': list_skill})
 
   
def choice_schedule(request, id_data_doctor):
    if request.method == 'GET':
        doctor = DoctorProfile.objects.get(id=id_data_doctor)
        opened_date = Schedule.objects.filter(user=doctor.user).filter(date__gte=datetime.now()).filter(is_checked=False)
        return render(request, 'choice_schedule.html', {'doctor': doctor, 'opened_date': opened_date})


def schedule_time(request, id_date_open):
    if request.method == 'GET':
        date_open = Schedule.objects.get(id=id_date_open)

        consultation = Consultation(
            patient=request.user,
            opened_date=date_open
        )

        date_open.is_checked=True
        consultation.save()

        messages.add_message(request, constants.SUCCESS, 'Consulta realizada com sucesso!')
        return redirect('/patient/my_consultation')
    

def my_consultation(request):
    if request.method == 'GET':
        # O __gte é uma expressao para capturar os dados que forem MAIOR OU IGUAL se voce for usar menor ou igual voce pode usar __lte ou se for apenas maior seria __gt e menor seria __lt.
        my_consultation = Consultation.objects.filter(patient=request.user).filter(opened_date__date__gte=datetime.now())
        return render(request, 'my_consultation.html', {'my_consultation': my_consultation})