from django.urls import path
from gruposApp import views


from django.contrib.auth.decorators import login_required

urlpatterns = [
   
    path('proveedores-grupo', login_required(views.seleccionarProveedor), name="Grupo-SeleccionProveedor"),
    path('grupos/<int:idProveedor>', login_required(views.crearGrupo), name="CrearGrup"),
    
    path('gruposProveedor/<int:idProveedor>', login_required(views.gruposProveedor), name="GruposProveedor"),
    
    
    path('eliminarGrupo/<int:idGrupo>/<int:idProveedor>', login_required(views.eliminarGrupo), name="EliminarGrupo"),
    
    
    path('editarGrupo/<int:idGrupo>/<int:idProveedor>', login_required(views.editarGrupo), name="EditarGrupo"),


    

]