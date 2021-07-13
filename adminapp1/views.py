from django.shortcuts import render,redirect

from core.models import Noticia,Categoria
from core.forms import NoticiaForm,CategoriaForm



# Create your views here.

def inicio(request):
    noticias = Noticia.objects.all()
    datos = {
        'listanoticias': noticias
    }

    return render(request,'core/inicio.html',datos)


def Crear(request):
    datos = {
        'form':NoticiaForm()
    }
    if request.method == 'POST':
        formulario = NoticiaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"
    return render(request,'core/Crear.html',datos)

def Modificar(request,id):
    noticia = Noticia.objects.get(idNoticia=id)
    datos = {
        'form':NoticiaForm(instance=noticia)
    }
    if request.method == 'POST':
        formulario = NoticiaForm(data=request.POST, instance=noticia)
        if formulario.is_valid:
             formulario.save()
             datos['mensaje'] = "Modificado correctamente"
    return render(request,'core/Modificar.html',datos)

def Eliminar(request,id):
    noticia = Noticia.objects.get(idNoticia = id)
    noticia.delete();

    return redirect(to="inicio")

def inicioC(request):
    categoria = Categoria.objects.all()
    datos = {
        'listacategoria': categoria
    }

    return render(request,'core/inicioC.html',datos)


def CrearC(request):
    datos = {
        'form':CategoriaForm()
    }
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"
    return render(request,'core/CrearC.html',datos)

def ModificarC(request,id):
    categoria = Categoria.objects.get(idCategoria=id)
    datos = {
        'form':CategoriaForm(instance=categoria)
    }
    if request.method == 'POST':
        formulario = CategoriaForm(data=request.POST, instance=categoria)
        if formulario.is_valid:
             formulario.save()
             datos['mensaje'] = "Modificado correctamente"
    return render(request,'core/ModificarC.html',datos)

def EliminarC(request,id):
    categoria = Categoria.objects.get(idCategoria = id)
    categoria.delete();

    return redirect(to="inicioC")