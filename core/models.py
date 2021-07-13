from django.db import models
from django.db.models.base import Model


# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name="id de la categoria ")
    nombreCategoria = models.CharField(max_length=50,verbose_name="Nombre de la categoria ")

    def __str__(self):
        return self.nombreCategoria

class Noticia(models.Model):
    idNoticia = models.IntegerField(primary_key=True,verbose_name="id de noticia ")
    nombreNoticia = models.CharField(max_length=50,verbose_name="Nombre de la noticia ")
    descripcionNoticia = models.CharField(max_length=200,verbose_name="descripcion de la noticia ")
    imagenNoticia = models.CharField(max_length=200,verbose_name="imagen de la noticia")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)


    def __str__(self):
        return self.nombreNoticia 

class Usuarios(models.Model):
    idUsuario = models.IntegerField(primary_key=True,verbose_name="id de usuario ")
    nombreUsuario = models.CharField(max_length=50,verbose_name="Nombre de Usuario ")
    contrasenaUsuario = models.CharField(max_length=50,verbose_name="Contraseña")

    def __str__(self):
        return self.nombreUsuario


