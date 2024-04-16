from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth

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
        return redirect('/users/login')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Usamos o auth nativo do django para saber se esse usuario esta no banco de dados, ou seja, ele ira fazer a autenticação do usuario e verificar se esse usuario pode fazer o login ou nao.
        user = auth.authenticate(request, username=username, password=password)

        # Aqui estamos verificando se o usuario estiver de fato autenticado, sera armazenado os dados em sections para que ele permaneca conectato aque ele ele faça o logout.
        # Depois estamos usando novamente o auth nativo do django para armazenar os dados do usuario autenticado para que ele permaneça com a sessao aberta.
        if user:
            auth.login(request, user) 
            return redirect('/patient/home')
        
        messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos')
        return redirect('users/login')


# Para podermos fazer o logout é simples e iremos usar o auth nativo do django novamente que ira atraves da request verificar se tem usuario logado e ira interromper a section.
def logout(request):
    auth.logout(request)
    return redirect('users/login')

