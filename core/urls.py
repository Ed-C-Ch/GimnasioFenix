from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="index"),
    path('home', views.home, name="home"),
    path('contacto', views.contacto, name="contacto"),
    path('sinServicio', views.sinServicio, name="sinServicio"),
]