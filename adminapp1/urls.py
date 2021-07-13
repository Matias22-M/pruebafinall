from .views import inicio,Crear,Modificar,Eliminar,inicioC,CrearC,ModificarC,EliminarC

urlpatterns = [

    
    path('inicio',inicio,name="inicio"),
    path('Crear',Crear,name="Crear"),
    path('Modificar/<id>',Modificar,name="Modificar"),
    path('Eliminar/<id>',Eliminar,name="Eliminar"),
    path('inicioC',inicioC,name="inicioC"),
    path('CrearC',CrearC,name="CrearC"),
    path('ModificarC/<id>',ModificarC,name="ModificarC"),
    path('EliminarC/<id>',EliminarC,name="EliminarC"),
    
    
]