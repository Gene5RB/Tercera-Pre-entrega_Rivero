from django import forms

class ProyectoFormulario (forms.Form):

    nombre= forms.CharField()
    codigo= forms.CharField()
    descripcion= forms.CharField()
    fechaRealizacion= forms.CharField()

