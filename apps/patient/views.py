from django.shortcuts import render
from datetime import datetime

#IMPORTS MODELS
from doctors.models import DoctorProfile, Skills, Schedule

def home(request):
    if request.method == 'GET':
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
