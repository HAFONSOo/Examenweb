from django.db import models

# Create your models here.
class Producto(models.Model):
     idProducto=models.AutoField(primary_key=True)
     nombre=models.CharField(max_length=200)
     precio=models.IntegerField()
     descripcion=models.CharField(max_length=200)
def __str__(self):
    texto="{0}({1})"
    return texto.format(self.nombre,self.Precio,self.Descripcion)