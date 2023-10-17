from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse
from DogsApp.forms import form_adoptado
from DogsApp.models import Adoptado
from DogsApp.forms import form_adoptante
from DogsApp.models import Adoptante
from DogsApp.forms import form_refugio
from DogsApp.models import Refugio
from DogsApp.forms import formbusqueda_adoptado



# Create your views here.

def inicioview(request):	
    return render(request,"temp_app/inicio.html")

def pruebaview(request):	
    return HttpResponse("Hola Susy")		

def pruebaview2(request):	
    return render(request,"temp_app/prueba2.html")
   

def adoptado_view(request):	
    if request.method == "POST":	
       candidato=form_adoptado(request.POST)
       
       print(candidato)
       
       if candidato.is_valid:
           informacion = candidato.cleaned_data
           postulante= Adoptado(informacion["animal"], informacion["nombre"], informacion["edad"])
           postulante.save()	
           return render(request,"temp_app/inicio.html")	
       
    else:
       candidato = form_adoptado()     
       return render(request,"temp_app/form_adoptado.html", {"candidato":candidato})	

def adoptante_view(request):	
    if request.method == "POST":	
       candidato1=form_adoptante(request.POST)
       
       print(candidato1)
       
       if candidato1.is_valid:
           informacion1 = candidato1.cleaned_data
           postulante1= Adoptante(informacion1["apellido"], informacion1["email"])
           postulante1.save()	
           return render(request,"temp_app/inicio.html")	
       
    else:
       candidato1 = form_adoptante()     
       return render(request,"temp_app/form_adoptante.html", {"candidato1":candidato1})	
   
def refugio_view(request):	
    if request.method == "POST":	
       candidato2=form_refugio(request.POST)
       
       print(candidato2)
       
       if candidato2.is_valid:
           informacion2 = candidato2.cleaned_data
           postulante2= Refugio(["ID"],informacion2["ciudad"], informacion2["categoria"])
           postulante2.save()	
           return render(request,"temp_app/inicio.html")	
       
    else:
       candidato2 = form_refugio()     
       return render(request,"temp_app/form_refugio.html", {"candidato2":candidato2})	



# def buscardogview(request):
#     return render(request,"inicio/buscar_dog.html")

def busquedaview(request):
   
    candidato=formbusqueda_adoptado(request.GET)
              
    if candidato.is_valid:
          animal_a_buscar = candidato.cleaned_data.get("animal")
          animales_encontrados=Adoptado.objects.filter(animal__icontains=animal_a_buscar)
       	             
    else:
        animales_encontrados=Adoptado.objects.all  
    
    candidato = formbusqueda_adoptado()
    return render(request,"temp_app/buscar_dog.html", {"candidato":candidato,"animales_encontrados":animales_encontrados})	