from django import forms 
from django.forms import ModelForm
from .models import Noticia,Categoria

class NoticiaForm(ModelForm):
    class Meta:
        model = Noticia
        fields = ['idNoticia','nombreNoticia','descripcionNoticia','imagenNoticia','categoria']

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = ['idCategoria','nombreCategoria']
        