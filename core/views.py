from django import forms
from django.shortcuts import render, redirect
from . models import Comentarios
from . forms import ComentariosForm

def index(request):
    return render(request, 'core/index.html');

def home(request):
    return render(request, 'core/home.html');

def contacto(request):
    return render(request, 'core/contacto.html');

def sinServicio(request):
    return render(request, 'core/sinServicio.html');

def nosotros(request):
    return render(request, 'core/nosotros.html');

def clases(request):
    return render(request, 'core/clases.html');

def AgregarComentario(request):
    datos = {}
    if request.method == 'POST':
        formulario = ComentariosForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['form'] = formulario
            datos['mensaje'] = "Su mensaje ha sido guardado."
    else:
        datos['form'] = ComentariosForm()
    return render(request, 'core/contacto.html', datos);