from django.contrib import admin
from django.urls import path
from .views import * 
urlpatterns = [
    path('productos',mostrar_index,name="index"),
    path('registrarse',mostrar_registrarse,name="")
]
