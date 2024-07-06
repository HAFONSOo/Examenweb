from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto
def mostrar_index(request):
    Productos=Producto.objects.all()
    return render (request,'Productos.html',{"Productos":Productos} )
def mostrar_hombre(request):
    return render (request,'hombre.html' )
def mostrar_mujer(request):
    return render (request,'mujer.html' )
def mostrar_login(request):
    return render (request,'login.html' )
def mostrar_registrarse(request):
    return render (request,'registrarse.html' )
# Create your views here.
