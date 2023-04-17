from django.shortcuts import render
from django.http import HttpResponse
from .models import Proyectos   

# Create your views here.

def Proyecto(self, nombre, codigo, descripcion, fechaRealizacion):

    Proyecto1 = Proyectos(nombre=nombre, codigo=codigo, descripcion=descripcion, fechaRealizacion=fechaRealizacion)
    Proyecto1.save()
    
    return HttpResponse(f"""
    <p>Proyecto: {Proyecto1.nombre} -  Codigo: {Proyecto1.codigo} caragado con éxito</p>
    """)