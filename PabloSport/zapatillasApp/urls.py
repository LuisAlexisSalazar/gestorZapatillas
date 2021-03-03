from django.urls import path
from zapatillasApp import views


from django.contrib.auth.decorators import login_required

urlpatterns = [


    path('grupo-zapatillas/<int:tipoSeleccion>/<int:idProveedor>',
         login_required(views.mostrarGrupos), name="MostrarGrupos"),

    path('proveedor-grupo-zapatillas',
         login_required(views.mostrarProveedores), name="MostrarProveedores"),


    # CRUD ZAPATILLAS
    path('registrarZapatilla/<int:idGrupo>',
         login_required(views.registrarZapatilla), name="RegistrarZapatilla"),
    
    path('eliminarZapatilla/<int:idZapatilla>/<int:indicePagina>',
         login_required(views.eliminarZapatilla), name="EliminarZapatilla"),
    
    path('editarZapatilla/<int:idZapatilla>',
         login_required(views.editarZapatillas), name="EditarZapatilla"),




    # CRUD MARCAR
     path('crearMarca',
         views.crearMarca, name="CrearMarca"),
     
     path('editarMarca/<int:idMarca>',
         views.editarMarca, name="EditarMarca"),
     
     path('eliminarMarca/<int:idMarca>',
         views.eliminarMarca, name="EliminarMarca"),


     # Gaaaaa
     path('ga',
         views.getGa, name="Ga"),

]
