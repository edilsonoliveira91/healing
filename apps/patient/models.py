from django.db import models
from django.contrib.auth.models import User
from doctors.models import Schedule


class Consultation(models.Model):
    status_choices = (
        ('A', 'Agendada'),
        ('F', 'Finalizada'),
        ('C', 'Cancelada'),
        ('I', 'Iniciada')
    )
    patient = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    opened_date = models.ForeignKey(Schedule, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=status_choices, default='A')
    link = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return self.patient.username
