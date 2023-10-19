from django.db import models

# Create your models here.

class Padrino(models.Model):
    apodo =models.CharField(max_length=50)
    ahijado = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_inicio = models.DateTimeField()
    
    def __str__(self) -> str:
        return f"{self.apodo} {self.ahijado}"