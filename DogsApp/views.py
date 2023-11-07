from django.shortcuts import render,redirect
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
from DogsApp.forms import UserEditForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from DogsApp.models import Avatar
from django.contrib.auth.decorators import permission_required
from django.views.generic.edit import FormView
from .forms import MessageForm
from DogsApp.models import Message
from DogsApp.forms import MessageForm
from DogsApp.forms import BlogPostForm
from DogsApp.models import BlogPost
from DogsApp.forms import AvatarForm








# Create your views here.

def inicioview(request):	
    return render(request,"temp_app/inicio.html")

def mascotasview(request):	
    return render(request,"temp_app/mascotas.html")

def usuarioview(request):	
    return render(request,"temp_app/usuario.html")


def aboutmeview(request):	
    return render(request,"temp_app/about_me.html")		

# def pruebaview2(request):	
#     return render(request,"temp_app/prueba2.html")
   

def adoptado_view(request):	
    if request.method == "POST":	
       candidato=form_adoptado(request.POST,request.FILES)
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
    if request.method == "POST" :	
       
       form=UserCreationFormCustom(request.POST)
       if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request,"temp_app/inicio.html", {"mensaje":"Usuario Creado"})   
    else:
       form = UserCreationFormCustom()    
        
    return render(request,"temp_app/registro.html", {"form":form})
  
# @permission_required('DogsApp.change_avatar')

def editarview(request):
    usuario = request.user
    try:
        avatar = Avatar.objects.get(user=usuario)
    except Avatar.DoesNotExist:
        avatar = Avatar(user=usuario)

    if request.method == "POST":

        form = UserEditForm(request.POST, instance=usuario)
        avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if form.is_valid() and avatar_form.is_valid():
            if usuario.has_perm('DogsApp.change_avatar'):
                avatar_anterior = Avatar.objects.filter(user=request.user)
                if (len(avatar_anterior) > 0):
                    avatar_anterior.delete()
                avatar_nuevo = Avatar(
                    user=request.user, imagen=avatar_form.cleaned_data["imagen"], descripcion=avatar_form.cleaned_data["descripcion"], link=avatar_form.cleaned_data["link"])
                avatar_nuevo.save()
                form.save()
        return redirect("inicio")
    else:
        form = UserEditForm(instance=usuario)
        avatar_form = AvatarForm(instance=avatar)

    return render(request, "temp_app/editar_perfil.html", {"form": form, "avatar_form": avatar_form})


# def editarview(request):
#     usuario=request.user
#     try:
#         avatar = Avatar.objects.get(user=usuario)
#     except Avatar.DoesNotExist:
#         avatar = Avatar(user=usuario)

#     if request.method == "POST":
        
#         form=UserEditForm(request.POST,request.FILES,instance=usuario)
#         avatar_form=AvatarForm(request.POST,request.FILES,instance=avatar)
#         print(avatar_form)
#         if form.is_valid() and avatar_form.is_valid():
#          if usuario.has_perm('DogsApp.change_avatar'):
#               if 'avatar' in request.FILES:  # Verificar si se ha cargado un nuevo avatar
#                     avatar_anterior = Avatar.objects.filter(user=request.user)
#                     if (len(avatar_anterior) > 0):
#                         avatar_anterior.delete()
#                     avatar_nuevo = Avatar(user=request.user, imagen=form.cleaned_data["avatar"], texto=form.cleaned_data["texto"],descripcion=avatar_form.cleaned_data["descripcion"], link=avatar_form.cleaned_data["link"])
#                     avatar_nuevo.save()
#                     form.save()
#         return redirect("inicio")


#             # if 'imagen' in request.FILES:  
#             #     avatar_form.save()
#             # form.save()
#             # return redirect("inicio")
#     else:
#         form = UserEditForm(instance=usuario)
#         avatar_form = AvatarForm(instance=avatar)

#     return render(request, "temp_app/editar_perfil.html",{"form":form, "avatar_form": avatar_form})

#

class cambiarpassview(LoginRequiredMixin,PasswordChangeView):
    template_name ="temp_app/cambiarpass.html"
    success_url = reverse_lazy("editar perfil")
    
def editaradoptadoview(request,adoptado_id):
    adoptado_a_editar = Adoptado.objects.get(id=adoptado_id)
    if request.method == "POST":
        form = form_adoptado(request.POST, request.FILES)
        if form.is_valid():
          
            adoptado_a_editar.animal = form.cleaned_data['animal']
            adoptado_a_editar.nombre = form.cleaned_data['nombre']
            adoptado_a_editar.edad = form.cleaned_data['edad']
            adoptado_a_editar.foto = form.cleaned_data.get('foto')
            adoptado_a_editar.save()

            return redirect("inicio")
    else:
      
        form = form_adoptado(initial={
            'animal': adoptado_a_editar.animal,
            'nombre': adoptado_a_editar.nombre,
            'edad': adoptado_a_editar.edad,
        })

    return render(request, "temp_app/editar_adoptado.html", {"form": form, "adoptado_id": adoptado_id})


    
    
    
    
    
    # candidato = form_adoptado(initial={"id":adoptado_a_editar.id,"animal":adoptado_a_editar.animal,"nombre":adoptado_a_editar.nombre, "edad":adoptado_a_editar.edad})
    # return render(request,"temp_app/editar_adoptado.html", {"form":form_adoptado})

def eliminaradoptadoview(request, adoptado_nombre):
    adoptado_a_eliminar = Adoptado.objects.get(id=adoptado_nombre)
    adoptado_a_eliminar.delete()
    contexto = {"adoptado a eliminar": adoptado_a_eliminar}
    return render(request, "temp_app/leer.html", contexto)





def detalledoptadoview(request,adoptado_id):
    adoptado = Adoptado.objects.get(id=adoptado_id)
    return render(request,"temp_app/detalle_adoptado.html", {"adoptado":adoptado})

def detalleusuarioview(request):
    return render(request,"temp_app/detalle_usuario.html", {"usuario":request.user})


# def detalleusuarioview(request,usuario_id):
#     usuario = Avatar.objects.get(id=usuario_id)
#     return render(request,"temp_app/detalle_usuario.html", {"usuario":usuario})



def admin(request):	
    return render(request,"temp_app/admin.html")

class SendMessageView(FormView):
    template_name = 'temp_app/send_message.html'
    form_class = MessageForm
    success_url = reverse_lazy("listado")

    def form_valid(self, form):
        message = form.save(commit=False)
        message.sender = self.request.user
        message.save()
        return super().form_valid(form)


class MessageListView(ListView):
    model = Message
    template_name = 'temp_app/message_list.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return Message.objects.filter(sender=self.request.user) | Message.objects.filter(receiver=self.request.user)
    
    
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('New Blog Successfully Added')
    else:
        form = BlogPostForm()
        context = {
            'form':form
        }

    return render(request, 'inicio.html', context)

