from django.shortcuts import render
from django.http import HttpResponse
from .models import Proyectos, Articulos, Clientes
from django import forms
from .forms import ProyectoFormulario

# Create your views here.

def Proyecto(self, nombre, codigo, descripcion, fechaRealizacion):

    Proyecto1 = Proyectos(nombre=nombre, codigo=codigo, descripcion=descripcion, fechaRealizacion=fechaRealizacion)
    Proyecto1.save()
    
    return HttpResponse(f"""
    <p>Proyecto: {Proyecto1.nombre} -  Codigo: {Proyecto1.codigo} caragado con éxito</p>
    """)

def inicio(self):
    return render(self, "inicio.html")

def Proyectos(self):
    return render(self, "proyectos.html")

def Articulos(self):
    return render(self, "articulos.html")

def Clientes(self):
    return render(self, "clientes.html")

def ProyectoFormulario(request):
   
   if request.method == "POST":
        Formulario1 = ProyectoFormulario(request.POST)
        print(Formulario1)

        if Formulario1.is_valid:
            informacion = Formulario1.cleaned_data
            proyecto = Proyectos(nombre=informacion["nombre"], codigo=informacion["codigo"], descripcion=informacion["descripcion"], fechaRealizacion=informacion["fechaRealizacion"])
            proyecto.save()
            
            return render(request, "inicio.html")
   else:
        Formulario1 = ProyectoFormulario()
        
        return render(request, "proyectoFormulario.html", {"Formulario1": Formulario1})

