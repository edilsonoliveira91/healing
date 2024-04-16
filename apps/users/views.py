from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

#IMPORT MESSAGES
from django.contrib import messages
from django.contrib.messages import constants


def create_user(request):
    if request.method == 'GET':
        return render(request, 'create_user.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password != password_confirm:
            messages.add_message(request, constants.ERROR, 'A senhas não são iguais.')
            return redirect('/users/create_user')
        
        if len(password) < 6:
            messages.add_message(request, constants.ERROR, 'A senha tem que conter mais de 6 caracteres.')
            return redirect('/users/create_user')
        
        # Validando para saber se o usuario ja existe.
        user = User.objects.filter(username=username)
        if user.exists():
            messages.add_message(request, constants.ERROR, 'Esse usuario já existe. Tente outro nome.')
            return redirect('/users/create_user')
        
        # Criando e salvando usuario usando o create_user do django
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso!')
        return redirect('/users/create_user')


