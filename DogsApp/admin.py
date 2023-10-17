from django.contrib import admin
from django import forms

# Register your models here.
class formestudiante(forms.Form):	

     Nombre = forms.CharField(max_length=10)
     Email = forms.EmailField()
     
    
class formcurso(forms.Form):		
    Nombre_curso = forms.CharField( max_length=10, required=False)
    Numero=forms.IntegerField

class formbiblio(forms.Form):	
  Libro = forms.CharField( max_length=50, required=False)
  Editorial = forms.CharField( max_length=50, required=False) 