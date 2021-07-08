from django.urls import path
from .views import index,noticiasP

urlpatterns = [
    path('',index,name="index"),
    path('noticiasP/',noticiasP,name="noticiasP"),
]