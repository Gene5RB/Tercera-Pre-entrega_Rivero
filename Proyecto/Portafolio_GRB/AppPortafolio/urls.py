from django.contrib import admin
from django.urls import path
from AppPortafolio.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('proyectos/', Proyectos, name="Portafolio"),
    path('clientes/', Clientes, name="Clientes"),
    path('articulos/', Articulos, name="Articulos"),
    path('proyectoForm/', ProyectoFormulario, name="ProyectoFormulario"),  
]