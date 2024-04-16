from django.db import models
from django.contrib.auth.models import User


# Criamos uma funcao para retornar se o usuario é um medico cadastrado (existente).
def is_doctor(user):
    return DoctorProfile.objects.filter(user=user).exists()

class Skills(models.Model):
    skill = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.skill


class DoctorProfile(models.Model):
    crm = models.IntegerField() # São apenas 7 digitos.
    name = models.CharField(max_length=100)
    cep = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    number = models.IntegerField()
    # Agora temos que salvar o pdf do rg mas no banco de dados nos salvamos apenas o caminho e deixamos o arquivo salvo em uma pasta na aplicação.
    id_card = models.ImageField(upload_to='rgs')
    cedula_identidade_medica = models.ImageField(upload_to='cim')
    photo_profile = models.ImageField(upload_to='photo_perfil')
    note = models.TextField()
    appointment_cost = models.FloatField(default=100)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    skill = models.ForeignKey(Skills, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.user.username