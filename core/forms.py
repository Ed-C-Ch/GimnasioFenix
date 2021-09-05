from django import forms
from django.forms import ModelForm
from . models import Comentarios 

class ComentariosForm(ModelForm):
    class Meta:
        model = Comentarios
        fields = ['NombreUser', 'NumeroUser', 'EmailUser', 'Comentarios']
        widgets = {
            'NombreUser': forms.TextInput(attrs={'class': 'form-control'}),
            'NumeroUser': forms.NumberInput(attrs={'class': 'form-control'}),
            'EmailUser': forms.EmailInput(attrs={'class': 'form-control'}),
            'Comentarios': forms.Textarea(attrs={'class': 'form-control'}),
        }