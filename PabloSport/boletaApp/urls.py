from django.urls import path
from boletaApp import views

from django.contrib.auth.decorators import login_required

urlpatterns = [
   
    path('proveedor-grupo-boleta', login_required(views.seleccionarProveedor), name="Proveedor-grupo-boleta"),
    path('boleta/<int:tipoSeleccion>/<int:idProveedor>', login_required(views.seleccionarGrupos), name="Boletas"),

    path('CrearBoleta/<int:idGrupo>', login_required(views.crearBoleta), name="Boleta"),

]