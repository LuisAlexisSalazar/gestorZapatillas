from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.urls import reverse

# Importar los 2 modelos para las creaciones y asignacion de grupos a proveedores
from .models import Grupo, Proveedor
from boletaApp.models import Boleta

# Importar una funcion que nos da todo los proveedores
from proveedorApp.views import get_all_proveedores


from django.db.models import Count


# Create your views here.


def seleccionarProveedor(request):
    listaProveedores = Proveedor.objects.annotate(amount_grupos=Count('grupo'))

    return render(request, "gruposApp/seleccionarProveedor.html", {'proveedores': listaProveedores})


def crearGrupo(request, idProveedor):
    #  Crear un nuevo Grupo
    if request.method == "POST":
        fecha = request.POST["fecha"]

        proveedor = Proveedor.objects.annotate(
            amount_grupos=Count('grupo')).get(id=idProveedor)

        # Crear el grupo
        new_grupo = Grupo(fechaIngreso=fecha, creador=proveedor)
        new_grupo.save()

        grupos = Grupo.objects.filter(
            creador=idProveedor).order_by('-fechaIngreso')

        amount_boletas = Boleta.objects.filter(
            GrupoPerteneciente__creador=idProveedor).count()

        return render(request, "gruposApp/crearGrupos.html", {'grupos': grupos, 'proveedor': proveedor, 'cantidad_boletas': amount_boletas})

    # # Mostrar los grupos del proveedor seleccionado
    else:

        proveedor = Proveedor.objects.annotate(
            amount_grupos=Count('grupo')).get(id=idProveedor)

        grupos = Grupo.objects.filter(
            creador=idProveedor).order_by('-fechaIngreso')

        amount_boletas = Boleta.objects.filter(
            GrupoPerteneciente__creador=idProveedor).count()

        return render(request, "gruposApp/crearGrupos.html", {'grupos': grupos, 'proveedor': proveedor, 'cantidad_boletas': amount_boletas})


def gruposProveedor(request, idProveedor):

    proveedor = Proveedor.objects.annotate(
        amount_grupos=Count('grupo')).get(id=idProveedor)

    grupos = Grupo.objects.filter(
        creador=idProveedor).order_by('-fechaIngreso')

    return render(request, "gruposApp/gruposProveedor.html", {'grupos': grupos, 'proveedor': proveedor})


def eliminarGrupo(request, idGrupo, idProveedor):
    grupo = Grupo.objects.get(id=idGrupo)
    grupo.delete()

    return HttpResponseRedirect(reverse('CrearGrup', args=[idProveedor]))
    


def editarGrupo(request,idGrupo,idProveedor):
    if request.method == "POST":
        fecha = request.POST["fecha"]
        
        grupo=Grupo.objects.get(id=idGrupo)
        grupo.fechaIngreso=fecha
        grupo.save()


        return HttpResponseRedirect(reverse('CrearGrup',args=[idProveedor]))

    else:

        grupo=Grupo.objects.get(id=idGrupo)

        return render(request, "gruposApp/editarGrupo.html",{'grupo':grupo})