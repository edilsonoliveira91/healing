# Generated by Django 5.0.4 on 2024-04-16 09:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crm', models.IntegerField()),
                ('nome', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=15)),
                ('rua', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('rg', models.ImageField(upload_to='rgs')),
                ('cedula_identidade_medica', models.ImageField(upload_to='cim')),
                ('photo_perfil', models.ImageField(upload_to='photo_perfil')),
                ('note', models.TextField()),
                ('appointment_cost', models.FloatField(default=100)),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='doctors.skills')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
