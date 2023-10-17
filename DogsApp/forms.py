from django import forms

# from django.forms import Form
# from django.forms import ModelForm

class form_adoptado(forms.Form):	
     id=1
     animal = forms.CharField(max_length=15)
     nombre = forms.CharField()
     edad = forms.CharField()
     
class formbusqueda_adoptado(forms.Form):	
     id=1
     animal = forms.CharField(max_length=15, required=False)
    
                  
    
class form_adoptante(forms.Form):	
   	
   apellido = forms.CharField()
   email= forms.EmailField

class form_refugio(forms.Form):	
   
  ciudad = forms.CharField( )
  categoria = forms.CharField( ) 