from django.db import models

# Create your models here.

class Carrera(models.Model):
    nombre=models.CharField(max_length=25)
    codigo=models.IntegerField()


class Estudiante(models.Model):
    nombre=models.CharField(max_length=25)
    apellido=models.CharField(max_length=25)
    nmatricula=models.IntegerField()


class Materia(models.Model):
    nombre=models.CharField(max_length=25)
    comision=models.IntegerField()



class Examen(models.Model):
    nparcial=models.IntegerField()
    fechaDeRealizacion=models.DateField()
    notaobtenida=models.IntegerField()
    aprobado=models.BooleanField()
    