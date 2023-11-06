from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Padrino(models.Model):
    apodo =models.CharField(max_length=50)
    ahijado = models.CharField(max_length=50)
    descripcion = RichTextField()
    fecha_inicio = models.DateTimeField()
    
    def __str__(self) -> str:
        return f"{self.apodo} {self.ahijado}"