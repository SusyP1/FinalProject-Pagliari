from django import forms

# from django.forms import Form
# from django.forms import ModelForm

class form_adoptado(forms.Form):	

     animal = forms.CharField()
     nombre = forms.EmailField()
     edad = forms.IntegerField
     
    
class form_adoptante(forms.Form):		
   apellido = forms.CharField()
   email=forms.EmailField

class form_refugio(forms.Form):	
  ciudad = forms.CharField( )
  categoria = forms.CharField( ) 