from django.shortcuts import render, redirect

def index(request):
    return render(request, 'core/index.html');

def home(request):
    return render(request, 'core/home.html');

def contacto(request):
    return render(request, 'core/contacto.html');

def sinServicio(request):
    return render(request, 'core/sinServicio.html');