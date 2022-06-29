from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppProyectoFinal.models import Carrera, Estudiante, Materia, Examen
from AppProyectoFinal.forms import CarreraFormulario, EstudianteFormulario, MateriaFormulario, ExamenFormulario
# Create your views here.

def inicio(request):

    return render(request, "AppProyectoFinal/inicio.html")


def carrera(request):
   
   return render(request, "AppProyectoFinal/carrera.html")


def examen(request):
   
    return render(request, "AppProyectoFinal/examen.html")


def materias(request):

      if request.method == 'POST':

            miFormulario = MateriaFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  materia = Materia (nombre=informacion['nombre'], comision=informacion['comision']) 

                  materia.save()

                  return render(request, "AppProyectoFinal/inicio.html") 

      else: 

            miFormulario= EstudianteFormulario()

      return render(request, "AppProyectoFinal/materia.html", {"miFormulario":miFormulario})



def estudiantes(request):

      if request.method == 'POST':

            miFormulario = EstudianteFormulario(request.POST)

            print(miFormulario)

            if miFormulario.is_valid:

                  informacion = miFormulario.cleaned_data

                  estudiante = Estudiante (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   nmatricula=informacion['nmatricula']) 

                  estudiante.save()

                  return render(request, "AppProyectoFinal/inicio.html") 

      else: 

            miFormulario= EstudianteFormulario()

      return render(request, "AppProyectoFinal/estudiante.html", {"miFormulario":miFormulario})


def buscar(request):

      if  request.GET["carrera"]:

            codigo = request.GET['codigo'] 
            print(codigo)
            nombre = Carrera.objects.filter(codigo__icontains=codigo)
            print(nombre)
            return render(request, "AppProyectoFinal/inicio.html", {"nombre": nombre, "codigo":codigo })

      else: 

	      respuesta = "No enviaste datos"

      return render(request,"AppProyectoFinal/inicio.html", {"respuesta":respuesta})
