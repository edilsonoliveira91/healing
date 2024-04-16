from django.shortcuts import render, redirect
from .models import Skills, DoctorProfile, is_doctor

#IMPORT MESSAGES
from django.contrib import messages
from django.contrib.messages import constants

#IMPORTS DECORATORS
from django.contrib.auth.decorators import login_required


@login_required
def create_doctor(request):
    # Estamos verificando com a funcao criada na models para indentificar se o usuario ja é um medico cadastro pois ele nao pode criar 2 vezes o mesmo cadastro.
    if is_doctor(request.user):
        messages.add_message(request, constants.ERROR, 'Você já é um medico cadastrado!')
        return redirect('doctors/schedule_appointment')

    if request.method == 'GET':
        list_skills = Skills.objects.all()
        return render(request, 'create_doctor.html',{'list_skill': list_skills})
    elif request.method == 'POST':
        crm = request.POST.get('crm')
        cim = request.FILES.get('cim')
        name = request.POST.get('name')
        cep = request.POST.get('cep')
        address = request.POST.get('address')
        zone = request.POST.get('zone')
        number = request.POST.get('number')
        id_card = request.FILES.get('id-card')
        photo_profile = request.FILES.get('photo_profile')
        skill = request.POST.get('skill')
        note = request.POST.get('note')
        appointment_cost = request.POST.get('appointment_cost')

    doctor_profile = DoctorProfile(
        crm=crm,
        cedula_identidade_medica=cim,
        name=name,
        cep=cep,
        address=address,
        zone=zone,
        number=number,
        id_card=id_card,
        photo_profile=photo_profile,
        skill_id=skill,
        note=note,
        appointment_cost=appointment_cost,
        user=request.user
    )

    doctor_profile.save()
    messages.add_message(request, constants.SUCCESS, 'Cadastro medico salvo com sucesso!')
    return redirect('doctors/schedule_appointment')
