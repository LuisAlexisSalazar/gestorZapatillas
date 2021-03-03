from django.urls import path
from ventaApp import views

from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    path('codigo', login_required(views.recibirCodigo), name="CodigoVenta"),
    path('caracteristicas', login_required(views.recibirCaracteristicas), name="CaracteristicasVenta"),
    
    path('zapatillasGeneralesVender', login_required(views.zapatillasGenerales), name="ZapatillasGeneralesVender"),

    # CRUD Venta
    path('crearVenta/<int:idZapatilla>', login_required(views.crearVenta), name="CrearVenta"),

    path('eliminarVenta/<int:idVenta>', login_required(views.eliminarVenta), name="EliminarVenta"),

    path('editarVenta/<int:idVenta>', login_required(views.editarVenta), name="EditarVenta"),



]