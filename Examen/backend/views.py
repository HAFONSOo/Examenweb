from django.http import HttpResponse
from django.shortcuts import render

from .models import Producto
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .serializer import *
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from django.db import transaction
from django.utils.decorators import method_decorator



class JSONResponseOkRows(HttpResponse):
    def __init__(self, data,msg, **kwargs):
        #print(len(data))
        data= {"OK":True,"count":len(data),"registro":data,"msg":msg}
        #print("data",data)
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseOkRows, self).__init__(content, **kwargs)

class JSONResponseOk(HttpResponse):
    def __init__(self, data, msg, **kwargs):
        data = {"OK": True, "count": "1", "registro": data, "msg": msg}
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseOk, self).__init__(content, **kwargs)

class JSONResponseErr(HttpResponse):
    def __init__(self, data, msg, **kwargs):
        data = {"OK": False, "count": "0", "registro": data, "msg": msg}
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponseErr, self).__init__(content, **kwargs)




def mostrar_index(request):
    Productos=Producto.objects.all()
    return render (request,'Productos.html',{"Productos":Productos} )



class producto:
    @csrf_exempt
    def agregar_producto(request):
        if request.method == 'POST':
            data = json.loads(request.body)
            serializer = ProductoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JSONResponseOk(serializer.data, "Producto agregado exitosamente")
            else:
                return JSONResponseErr(serializer.errors, "Error al agregar el producto")
        else:
            return JSONResponseErr(None, "Solo se aceptan solicitudes POST")
        
    def obtener_productos(request):
        if request.method == 'GET':
            # Solo obtén los productos que están activos
            productos = Producto.objects.filter()
            lista_productos = list(productos.values('idProducto', 'nombre', 'precio', 'descripcion'))  
            return JSONResponseOkRows(lista_productos, "Productos obtenidos exitosamente")
        else:
            return JSONResponseErr(None, "Solo se aceptan solicitudes GET")

    def obtener_producto(request,id):
        if request.method == 'GET':
            # Solo obtén los productos que están activos
            productos = Producto.objects.filter(activo=True, id=idProducto)
            lista_productos = list(productos.values('idProducto', 'nombre', 'precio', 'descripcion'))  # incluye 'codigo' y 'precio'
            if lista_productos:
                return JSONResponseOk(lista_productos[0], "Producto obtenido exitosamente")
            else:
                return JSONResponseErr(None, "Producto no encontrado")
        else:
            return JSONResponseErr(None, "Solo se aceptan solicitudes GET")

    @csrf_exempt
    def modificar_producto(request, id):
        if request.method == 'PUT':
            # Parsea los datos del request
            data = JSONParser().parse(request)

            # Busca el producto por su código
            try:
                producto = Producto.objects.get(id=idProducto)
            except Producto.DoesNotExist:
                # Si el producto no existe, devuelve un error
                return JSONResponseErr(data={}, msg='Producto no encontrado', status=404)

            # Actualiza los datos del producto
            serializer = ProductoSerializer(producto, data=data, partial=True)  # `partial=True` permite actualizaciones parciales
            if serializer.is_valid():
                serializer.save()
                return JSONResponseOk(serializer.data, msg='Producto actualizado exitosamente')
            return JSONResponseErr(serializer.errors, msg='Error al actualizar el producto', status=400)
        
    @csrf_exempt
    def eliminar_producto(request, id):
        if request.method == 'DELETE':
            try:
                # Busca el producto por su código
                producto = Producto.objects.get(id=idProducto)
            except Producto.DoesNotExist:
                # Si el producto no existe, devuelve un error
                return JSONResponseErr(data={}, msg='Producto no encontrado', status=404)

            # Desactiva el producto
            producto.activo = False
            producto.save()

            # Devuelve una respuesta de éxito
            return JSONResponseOk(data={}, msg='Producto desactivado exitosamente', status=200)

# Create your views 
