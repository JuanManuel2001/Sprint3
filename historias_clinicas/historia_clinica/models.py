from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone



class Paciente(models.Model):
    nombre = models.CharField(max_length=100, default='')
    apellido = models.CharField(max_length=100,default='')
    fecha_nacimiento = models.DateField(null=True, blank=True)
    dni = models.CharField(max_length=20)
    obra_social = models.CharField(max_length=100)

    def clean(self):
        if self.fecha_nacimiento and self.fecha_nacimiento > timezone.now().date():
            raise ValidationError('La fecha de nacimiento no puede ser futura')

    class Meta:
        app_label = 'historia_clinica'
    



class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)

    class Meta:
        app_label = 'historia_clinica'


class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateField(null=True, blank=True)
    descripcion = models.TextField()

    class Meta:
        app_label = 'historia_clinica'
    def __str__(self):
        return f'{self.paciente} - {self.medico} - {self.fecha}'


class HistoriaClinicaAuditada(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateField(null=True, blank=True)
    descripcion = models.TextField()
    usuario_creacion = models.CharField(max_length=100)
    usuario_modificacion = models.CharField(max_length=100)

    class Meta:
        app_label = 'historia_clinica'


class PacienteAuditado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    dni = models.CharField(max_length=20)
    obra_social = models.CharField(max_length=100)
    usuario_creacion = models.CharField(max_length=100)
    usuario_modificacion = models.CharField(max_length=100)

    class Meta:
        app_label = 'historia_clinica'


class MedicoAuditado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    matricula = models.CharField(max_length=100)
    usuario_creacion = models.CharField(max_length=100)
    usuario_modificacion = models.CharField(max_length=100)

    class Meta:
        app_label = 'historia_clinica'