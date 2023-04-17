from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader

def saludo(request):
    return HttpResponse("Hola Django-Coder")

def MiNombreEs(self,nombre):
    documentoDeTexto = f"Mi nombre es: <br><br> {nombre}"
    return HttpResponse(documentoDeTexto)

def probandoTemplate(self):
    nom = "Nicólas"
    ap = "Peréz"

    diccionario ={"nombre":nom, "apellido": ap}

    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

