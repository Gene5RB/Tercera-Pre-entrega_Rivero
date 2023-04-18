from django.urls import path
from AppPortafolio.views import *

urlpatterns = [
    path('', inicio),
    path('proyectos/', Proyectos),
    path('clientes/', Clientes),
    path('articulos/', Articulos),
    path('nuevo-proyecto/<nombre>/<codigo>/<descripcion>/<fechaRealizacion>', Proyecto),
   
]
