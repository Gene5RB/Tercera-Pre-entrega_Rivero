from django.db import models
import datetime

# Create your models here.
class Proyectos(models.Model):
    nombre=models.CharField(max_length=40)
    codigo=models.CharField(max_length=6)
    descripcion=models.TextField()
    fechaRealizacion=models.CharField(max_length=8)

    def __str__(self):
        return self.nombre

class Articulos(models.Model):
    titulo=models.CharField(max_length=40)
    fechaPubliacaion=models.DateField()

class Clientes(models.Model):
    nombreCliente=models.CharField(max_length=40)
    emailCliente=models.EmailField()
    mensajeCliente=models.CharField(max_length=300)
    nuevo=models.BooleanField()
    telCliente=models.CharField(max_length=15)

    def __str__(self):
        return self.nombreCliente