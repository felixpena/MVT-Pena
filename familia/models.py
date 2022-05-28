import datetime
from django.db import models
from django.utils import timezone

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre + ' ' + self.primer_apellido + ' ' + self.segundo_apellido + ' ' + str(self.edad) + ' ' + str(self.fecha_de_nacimiento)