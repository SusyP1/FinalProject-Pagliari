from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField 


 


# Create your models here.
class Adoptado(models.Model):	
    animal=models.CharField(max_length=15)
    nombre= models.CharField(max_length=15)
    edad= models.CharField(max_length=2, default=0,blank=True)
    foto=models.ImageField(upload_to="fotos_adoptados", null=True, blank=True)
    
    # def __str__(self) -> str:
    #     return f"{self.animal} {self.nombre}"
      
    
class Adoptante(models.Model):	
    apellido=models.CharField(max_length=40)		
    email = models.EmailField( max_length=20)
 
class Refugio(models.Model):	
    ciudad=models.CharField(max_length=40)		
    categoria=models.CharField(max_length=40)
    
class Avatar(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    def __str__(self):
        return f"{self.user} {self.imagen}"
    
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

 