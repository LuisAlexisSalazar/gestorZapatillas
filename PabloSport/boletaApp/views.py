from django.shortcuts import render
from boletaApp.models import Boleta, Grupo


from proveedorApp.models import Proveedor
from django.db.models import Count

# Create your views here.

# Funciones
def obtenerGruposGenerales():
    # Obtener descendetemente los grupos con el -
    listaGrupos = Grupo.objects.all().order_by('-fechaIngreso')
    return listaGrupos


def obtenerGruposEspecificos(idProveedor):
    print("LLamar funcion")
    proveedor = Proveedor.objects.get(id=idProveedor)
    listaGrupos = Grupo.objects.filter(creador=idProveedor)
    return listaGrupos


# Controladores
def seleccionarProveedor(request):

    listaProveedores = Proveedor.objects.all().annotate(amount_group=Count('grupo'))


    return render(request, "boletaApp/seleccionarProveedor.html", {'proveedores': listaProveedores})


def seleccionarGrupos(request, tipoSeleccion, idProveedor):

    # General
    if tipoSeleccion == 0:
        listaGrupos = obtenerGruposGenerales()

        # Podemos acceder a los datos de un modelo padre que sea foranea
        # for grupo in listaGrupos:
        #     print(grupo.creador.nombre)

        # Cambiar
        return render(request, "boletaApp/seleccionarGrupo.html", {'grupos': listaGrupos})

    # Especifica
    else:
        listaGrupos = obtenerGruposEspecificos(idProveedor)

        return render(request, "boletaApp/seleccionarGrupo.html", {'grupos': listaGrupos})


def crearBoleta(request, idGrupo):

    if request.method == "POST":

        # print("Post:")

        precio = request.POST["precio"]
        codigo = request.POST["codigo"]

        grupo = Grupo.objects.get(id=idGrupo)
        
        newBolata=Boleta(precio=precio,codigoBoleta=codigo,GrupoPerteneciente=grupo)
        newBolata.save()
        
        listaBoletas = Boleta.objects.filter(GrupoPerteneciente=grupo)

        return render(request, "boletaApp/crearBoleta.html",{'grupo': grupo , 'boletas':listaBoletas})

    else:
        grupo = Grupo.objects.get(id=idGrupo)
        listaBoletas = Boleta.objects.filter(GrupoPerteneciente=grupo)

        # return render(request,"boletaApp/ga.html")
        return render(request, "boletaApp/crearBoleta.html", {'grupo': grupo , 'boletas':listaBoletas})
