from django.urls import path
from proveedorApp import views


from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    path('base', login_required(views.base), name="Base"),
    path('proveedor', login_required(views.IngresarProveedor), name="Proveedor"),

    path('eliminarProveedor/<int:idProveedor>',login_required(views.eliminarProveedor),name="EliminarProveedor"),
    
    path('editarProveedor/<int:idProveedor>',login_required(views.editarProveedor),name="EditarProveedor"),
   
    path('eliminarProveedor/<int:idGrupo>/<int:idProveedor>',login_required(views.eliminarProveedor),name="EliminarProveedor"),

]