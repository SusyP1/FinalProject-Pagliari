from django.db import models
from django.db.models import Model


# Create your models here.
class Adoptado(models.Model):	
  
    animal=models.CharField(max_length=15)
    nombre= models.CharField(max_length=15)
    edad = models.IntegerField
    
class Adoptante(models.Model):	
    	
    apellido=models.CharField(max_length=40)		
    email = models.EmailField( max_length=20)
 
class Refugio(models.Model):	
    
    ciudad=models.CharField(max_length=40)		
    categoria=models.CharField(max_length=40)
 