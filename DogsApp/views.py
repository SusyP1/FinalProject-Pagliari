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
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,authenticate
from DogsApp.forms import UserCreationFormCustom



# Create your views here.

def inicioview(request):	
    return render(request,"temp_app/inicio.html")

# def pruebaview(request):	
#     return HttpResponse("Hola Susy")		

# def pruebaview2(request):	
#     return render(request,"temp_app/prueba2.html")
   

def adoptado_view(request):	
    if request.method == "POST":	
       candidato=form_adoptado(request.POST)
       print(candidato)
       if candidato.is_valid:
           informacion = candidato.cleaned_data
           postulante= Adoptado(animal=informacion["animal"],nombre=informacion["nombre"],edad=informacion["edad"])
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
          animal_a_buscar = candidato.get("animal")
          animales_encontrados=Adoptado.objects.filter(animal__icontains=animal_a_buscar)
       	             
    else:
        animales_encontrados=Adoptado.objects.all  
    
    candidato = formbusqueda_adoptado()
    return render(request,"temp_app/buscar_dog.html", {"candidato":candidato,"animales_encontrados":animales_encontrados})	

def leerview(request):
    adoptados=Adoptado.all()
    contexto={"adoptados":adoptados}
    return render(request,"temp_app/leer.html", contexto)	

def loginview(request):
    if request.method == "POST":	
       form=AuthenticationForm(request,data = request.POST)
       
             
       if form.is_valid:
          usuario = form.cleaned_data.get("username")
          contraseña= form.cleaned_data.get("password")
          email=form.cleaned_data.get("email")
          
          user=authenticate(username=usuario,password=contraseña,email=email)
          login(request,user)
          
      	
          return render(request,"temp_app/inicio.html", {"mensaje":f"Bienvenido {user.username}"})
       
    else:
       form = AuthenticationForm()     
       return render(request,"temp_app/login.html", {"form":form})	
   
def registroview(request):
    if request.method == "POST":	
       
       form=UserCreationFormCustom(request.POST)
    
       if form.is_valid:
            username = form.cleaned_data("username")
            form.save()
            return render(request,"temp_app/inicio.html", {"mensaje":"Usuario Creado"})
    
          
    else:
       form = UserCreationFormCustom()     
       return render(request,"temp_app/registro.html", {"form":form})