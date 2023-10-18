from django import forms
from django.contrib.auth.forms import  UserCreationForm,UserModel

# from django.forms import Form
# from django.forms import ModelForm

class form_adoptado(forms.Form):	
   animal = forms.CharField(max_length=15)
   nombre = forms.CharField()
   edad = forms.CharField(max_length=2)
     
class formbusqueda_adoptado(forms.Form):	
   animal = forms.CharField(max_length=15, required=False)
    
                 
    
class form_adoptante(forms.Form):	
   	
   apellido = forms.CharField()
   email= forms.EmailField

class form_refugio(forms.Form):	
   
  ciudad = forms.CharField( )
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
      
   