from core.forms import NoticiaForm
from django.http import request
from django.shortcuts import render,redirect
from .models import Noticia


# Create your views here.


def index(request):
    noticias = Noticia.objects.all()
    datos = {
        'listanoticias': noticias
    }

    return render(request,'core/index.html',datos)

def login(request):
    noticias = Noticia.objects.all()
    datos = {
        'listanoticias': noticias
    }
    return render(request,'registration/login.html')

def noticiasP(request,id):
    noticia = Noticia.objects.get(idNoticia=id)
    datos = {
        'form':NoticiaForm(instance=noticia)
    }
 
    return render(request,'core/noticiasP.html',datos)







