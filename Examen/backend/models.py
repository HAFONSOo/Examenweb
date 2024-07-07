from django.db import models
from rest_framework import serializers

# Create your models here.
class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    imagen = models.URLField(null=True, blank=True)  

   
