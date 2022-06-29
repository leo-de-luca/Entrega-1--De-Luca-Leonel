from django.contrib import admin

from AppProyectoFinal.models import Carrera, Estudiante, Examen, Materia

# Register your models here.



admin.site.register(Carrera)

admin.site.register(Estudiante)

admin.site.register(Materia)

admin.site.register(Examen)