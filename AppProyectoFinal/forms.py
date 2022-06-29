from unittest.util import _MAX_LENGTH
from django import forms 


class CarreraFormulario(forms.Form):
    nombre=forms.CharField(max_length=25)
    codigo=forms.IntegerField()




class EstudianteFormulario(forms.Form):
    nombre=forms.CharField(max_length=25)
    apellido=forms.CharField(max_length=25)
    nmatricula=forms.IntegerField()




class MateriaFormulario(forms.Form):
    nombre=forms.CharField(max_length=25)
    comision=forms.IntegerField()



class ExamenFormulario(forms.Form):
    nparcial=forms.IntegerField()
    fechaDeRealizacion=forms.DateField()
    notaobtenida=forms.IntegerField()
    aprobado=forms.BooleanField()

