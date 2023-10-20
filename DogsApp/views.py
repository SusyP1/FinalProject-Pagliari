from django.shortcuts import render,redirect
from django.template import Template, Context
from django.http import HttpResponse
from DogsApp.forms import form_adoptado
from DogsApp.models import Adoptado
# from DogsApp.forms import form_adoptante
# from DogsApp.models import Adoptante
from DogsApp.forms import form_refugio
from DogsApp.models import Refugio
from DogsApp.forms import formbusqueda_adoptado
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,authenticate
from DogsApp.forms import UserCreationFormCustom
from DogsApp.forms import UserEditForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView




# Create your views here.

def inicioview(request):	
    return render(request,"temp_app/inicio.html")

def mascotasview(request):	
    return render(request,"temp_app/mascotas.html")

def usuarioview(request):	
    return render(request,"temp_app/usuario.html")


def aboutmeview(request):	
    return HttpResponse("Me llamo Susana Pagliari, tengo 41 años , 2 hijos y muchas mascotas caballos, burros, perros , gatos , ovejas , patos y gansos. Esta es la primera vez que hago un curso de algo relacionado con programación , me ha resultado más dificil de lo que pensaba, pero me gusta mucho, si bien no toco nada de esto en mi trabajo(soy contadora), estoy segura que no va a ser el ultimo curso que haga")		

# def pruebaview2(request):	
#     return render(request,"temp_app/prueba2.html")
   

def adoptado_view(request):	
    if request.method == "POST":	
       candidato=form_adoptado(request.POST)
       print(candidato)
       if candidato.is_valid:
           informacion = candidato.cleaned_data
           postulante= Adoptado(animal=informacion["animal"],nombre=informacion["nombre"],edad=informacion["edad"],foto=informacion["foto"])
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
           postulante1= Adoptante(apellido=informacion1["apellido"], email=informacion1["email"])
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
           postulante2= Refugio(ciudad = informacion2["ciudad"], categoria=informacion2["categoria"])
           postulante2.save()	
           return render(request,"temp_app/inicio.html")	
       
    else:
       candidato2 = form_refugio()     
       return render(request,"temp_app/form_refugio.html", {"candidato2":candidato2})	



# def buscardogview(request):
#     return render(request,"inicio/buscar_dog.html")

def busquedaview(request):
    if request.method == "GET":
        candidato=formbusqueda_adoptado(request.GET)
              
        if candidato.is_valid():
          animal_a_buscar = candidato.cleaned_data.get("animal")
          animales_encontrados=Adoptado.objects.filter(animal__icontains=animal_a_buscar)
       	             
    else:
        animales_encontrados=Adoptado.objects.all  
    
    candidato = formbusqueda_adoptado()
    return render(request,"temp_app/buscar_dog.html", {"candidato":candidato,"animales_encontrados":animales_encontrados})	

def leerview(request):
    adoptados=Adoptado.objects.all()
    contexto={"adoptados":adoptados}
    return render(request,"temp_app/leer.html", contexto)	

def loginview(request):
    if request.method == "POST":	
       form=AuthenticationForm(request,data=request.POST)
       
             
       if form.is_valid():
          usuario = form.cleaned_data.get("username")
          contraseña= form.cleaned_data.get("password")
          email= form.cleaned_data.get("email")
          
          user=authenticate(username=usuario,password=contraseña,email=email)
          login(request,user)
          
      	
          return render(request,"temp_app/inicio.html", {"mensaje":f"Bienvenido {user.username}"})
       
    else:
       form = AuthenticationForm()     
       return render(request,"temp_app/login.html", {"form":form})	
   
def registroview(request):
    if request.method == "POST":	
       
       form=UserCreationFormCustom(request.POST)
    
       if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request,"temp_app/inicio.html", {"mensaje":"Usuario Creado"})
    
          
    else:
       form = UserCreationFormCustom()     
       return render(request,"temp_app/registro.html", {"form":form})
   
def editarview(request):
    
    usuario=request.user
    if request.method == "POST":	
       form=UserEditForm(request.POST,request.FILES,instance=usuario)
       if form.is_valid():
        avatar_anterior = Avatar.objects.filter(user=request.user)
        if (len(avatar_anterior) > 0):
            avatar_anterior.delete()
        avatar_nuevo = Avatar(
                user=request.user, imagen=form.cleaned_data["avatar"])
        avatar_nuevo.save()
        form.save()
        return redirect("inicio")
    else:
        form = UserEditForm(instance=usuario)

    return render(request, "temp_app/editar_perfil.html", {"form": form})

     
           
    #         form.save()
    #         return render(request,"temp_app/inicio.html")
    
    # else:
    #    form = UserEditForm(instance=request.user)     
    # return render(request,"temp_app/editar_perfil.html", {"form":form})

class cambiarpassview(LoginRequiredMixin,PasswordChangeView):
    template_name ="temp_app/cambiarpass.html"
    success_url = reverse_lazy("editar perfil")
    
def editaradoptadoview(request,adoptado_id):
    adoptado_a_editar = Adoptado.objects.get(id=adoptado_id)
    candidato = form_adoptado(initial={"id":adoptado_a_editar.id,"animal":adoptado_a_editar.animal,"nombre":adoptado_a_editar.nombre, "edad":adoptado_a_editar.edad})
    return render(request,"temp_app/editar_adoptado.html", {"form":form})

def eliminaradoptadoview(request,adoptado_nombre):
    adoptado_a_eliminar = Adoptado.objects.get(nombre=adoptado_nombre)
    adoptado_a_eliminar.delete()
    adoptado_a_eliminar = Adoptado.objects.all()
    contexto= {"adoptado a eliminar":adoptado_a_eliminar}
    return render(request,"temp_app/leer.html", contexto)

def admin(request):	
    return render(request,"temp_app/admin.html")