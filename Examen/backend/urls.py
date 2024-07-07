from django.contrib import admin
from django.urls import path
from .views import * 
urlpatterns = [
    path('productos',mostrar_index,name="index"),
    ##CRUD
    path('productos/agregar/', producto.agregar_producto, name='agregar_producto'),
    path('productos/obtener/', producto.obtener_productos, name='obtener_productos'),
    path('productos/obtener/<str:id>/', producto.obtener_producto, name='obtener_producto'),
    path('productos/modificar/<str:id>/', producto.modificar_producto, name='modificar_producto'),
    path('productos/eliminar/<str:id>/',producto.eliminar_producto, name='eliminar_producto'),

]
