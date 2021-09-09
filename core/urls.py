from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="index"),
    path('home', views.home, name="home"),

    path('sinServicio', views.sinServicio, name="sinServicio"),
    path('nosotros', views.nosotros, name="nosotros"),
    path('contacto', views.AgregarComentario, name="contacto"),
    path('clases', views.clases, name="clases"),
]