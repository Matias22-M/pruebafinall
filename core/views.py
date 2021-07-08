from django.shortcuts import render
from .models import Noticia


# Create your views here.


def index(request):
    noticias = Noticia.objects.all()
    datos = {
        'listanoticias': noticias
    }

    return render(request,'core/index.html',datos)

def noticiasP(request,id):
    noticias = Noticia.objects.get(idNoticia=id)
    datos = {
        'noticiap': noticias
    }

    return render(request,'core/noticiasP.html',datos)







