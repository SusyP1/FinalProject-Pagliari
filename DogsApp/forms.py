from django import forms
from django.contrib.auth.forms import  UserCreationForm,UserModel,UserChangeForm
from .models import Message
from .models import BlogPost
from .models import *


# from django.forms import Form
# from django.forms import ModelForm

class form_adoptado(forms.Form):	
   animal = forms.CharField(max_length=15)
   nombre = forms.CharField()
   edad = forms.CharField(max_length=2)
   foto = forms.ImageField(required=False)
   
     
class formbusqueda_adoptado(forms.Form):	
   animal = forms.CharField(max_length=15, required=False)
   

    

                  
    
class form_adoptante(forms.Form):	
   apellido = forms.CharField(max_length=40)
   email= forms.EmailField()

class form_refugio(forms.Form):	
   ciudad = forms.CharField(max_length=40)
   categoria = forms.CharField( ) 
  
class UserCreationFormCustom(UserCreationForm):
   username=forms.TextInput()
   email=forms.EmailField()
   password1=forms.CharField(label="Contraseña",widget=forms.PasswordInput)
   password2=forms.CharField(label="Repetir Contraseña",widget=forms.PasswordInput)
   class Meta:
      model = UserModel
      fields = ["username","email","password1","password2"]
      help_texts = {k:"" for k in fields}


   
class UserEditForm(UserChangeForm):
   password = None
   email=forms.EmailField(label="Ingrese su mail")
   username=forms.TextInput()
   last_name =forms.CharField(label="Apellido")
   first_name =forms.CharField(label="Nombre")
   
   class Meta:
      model = UserModel
      fields = ["email","last_name","first_name",]
      
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen',"descripcion","link"]

      
      
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'message']
        
        
class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('blog_title', 'blog_content')
        exclude = ['published_date']

      
