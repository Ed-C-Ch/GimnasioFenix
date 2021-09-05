from django.db import models

# Create your models here.

class Comentarios(models.Model):
    UserId = models.AutoField(primary_key=True)
    NombreUser = models.CharField(max_length=30)
    NumeroUser = models.IntegerField(null=True)
    EmailUser = models.EmailField(max_length=50)
    Comentarios = models.CharField(max_length=80)
    
    def __str__(self):
        return self.NombreUser