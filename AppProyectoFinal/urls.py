from django.urls import path

from AppProyectoFinal import views


urlpatterns = [

    path('',views.inicio, name="Inicio"),
    path('carrera',views.carrera, name="Carrera"),
    path('estudiante',views.estudiantes, name="Estudiante"),
    path('materia',views.materias, name="Materia"),
    path('examen',views.examen, name="Examen"),
    path('estudianteFormulario', views.estudiantes, name="EstudianteFormulario"),
    path('materiaFormulario', views.materias, name= "MateriaFormulario"),
    path('buscar/', views.buscar,),
    
]

