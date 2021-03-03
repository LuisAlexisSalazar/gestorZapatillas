from django.shortcuts import render,redirect


from .models import Grupo, Zapatilla, Proveedor, Marca
from django.db.models import Count
from boletaApp.views import obtenerGruposGenerales, obtenerGruposEspecificos



# Para entrar en otra url que no sea de mi app
from django.urls import reverse
from django.shortcuts import HttpResponseRedirect

# Create your views here.


def mostrarGrupos(request, tipoSeleccion, idProveedor):

    # General
    if tipoSeleccion == 0:

        listaGrupos = obtenerGruposGenerales().annotate(amount_zapatillas=Count('zapatilla'))
        return render(request, "zapatillasApp/seleccionarGrupo.html", {'grupos': listaGrupos})

    # Especifica
    else:
        listaGrupos = obtenerGruposEspecificos(idProveedor).annotate(amount_zapatillas=Count('zapatilla'))
        return render(request, "zapatillasApp/seleccionarGrupo.html", {'grupos': listaGrupos})


def mostrarProveedores(request):
    listaProveedores = Proveedor.objects.all().annotate(amount_group=Count('grupo'))

    return render(request, "zapatillasApp/seleccionarProveedor.html", {'proveedores': listaProveedores})


# CRUD de zapatillas
def registrarZapatilla(request, idGrupo):

    grupoEscogido = Grupo.objects.get(id=idGrupo)
    listaMarca = Marca.objects.all()

    if request.method == "POST":

        modelo = request.POST["modelo"]
        codigo = request.POST["codigo"]
        talla = request.POST["talla"]
        precioCompra = request.POST["precioCompra"]
        precioSugerido = request.POST["precioSuge"]
        categoriaGenero = request.POST["categoriaSelector"]
        categoriaUso = request.POST["categoriaUso"]
        colorPrincipal = request.POST["colorSelector"]
        marcaFormulario = request.POST["marca"]

        marca=Marca.objects.get(id=marcaFormulario)


        # opcionales
        descripcion = request.POST["descripcion"]
        descripcionColores = request.POST["coloresExtras"]

        newZapatilla = Zapatilla(modelo=modelo, codigo=codigo, talla=talla, precioSugerido=precioSugerido, precioCompra=precioCompra, categoriaGenero=categoriaGenero,
                                 categoriaUso=categoriaUso, descripcion=descripcion, colorPrincipal=colorPrincipal, colorSecundario=descripcionColores, grupoPerteneciente=grupoEscogido,marcaPerteneciente=marca)

        newZapatilla.save()

        listaZapatillas = Zapatilla.objects.filter(
            grupoPerteneciente=grupoEscogido)

        return render(request, "zapatillasApp/registrarZapatilla.html", {"idGrupo": idGrupo, "zapatillas": listaZapatillas, 'marcas': listaMarca})

    else:

        listaZapatillas = Zapatilla.objects.filter(
            grupoPerteneciente=grupoEscogido)

        

        return render(request, "zapatillasApp/registrarZapatilla.html", {'idGrupo': idGrupo, 'zapatillas': listaZapatillas, 'marcas': listaMarca})


# Gestionar las url
def regresarPagina(request, idGrupo, indicePagina):

    # regresar al html de registrar zapatilla
    if indicePagina == 0:
        return HttpResponseRedirect(reverse('RegistrarZapatilla', args=[idGrupo]))

    elif indicePagina == 1:
        return HttpResponseRedirect(reverse('Grupo-SeleccionProveedor'))


def eliminarZapatilla(request, idZapatilla, indicePagina):
    zapatillaEscogida = Zapatilla.objects.get(id=idZapatilla)

    # la pk es lo mismo que el ID = PK
    # idGrupo = zapatillaEscogida.pk

    idGrupo = zapatillaEscogida.grupoPerteneciente.id
    zapatillaEscogida.delete()

    return regresarPagina(request, idGrupo, indicePagina)


def editarZapatillas(request,idZapatilla):
    zapatilla=Zapatilla.objects.get(id=idZapatilla)
    listaMarcas=Marca.objects.all()

    if request.method == "POST":


        modelo = request.POST["modelo"]
        codigo = request.POST["codigo"]
        talla = request.POST["talla"]
        precioCompra = request.POST["precioCompra"]
        precioSugerido = request.POST["precioSuge"]
        categoriaGenero = request.POST["categoriaSelector"]
        categoriaUso = request.POST["categoriaUso"]
        colorPrincipal = request.POST["colorSelector"]
        marcaFormulario = request.POST["marca"]

        marca=Marca.objects.get(id=marcaFormulario)

        # opcionales
        descripcion = request.POST["descripcion"]
        descripcionColores = request.POST["coloresExtras"]


        zapatilla.modelo=modelo
        zapatilla.codigo=codigo
        zapatilla.talla=talla
        zapatilla.precioSugerido=precioSugerido 
        zapatilla.precioCompra=precioCompra
        zapatilla.categoriaGenero=categoriaGenero
        zapatilla.categoriaUso=categoriaUso
        zapatilla.descripcion=descripcion
        zapatilla.colorPrincipal=colorPrincipal
        zapatilla.colorSecundario=descripcionColores
        zapatilla.marcaPerteneciente=marca

        zapatilla.save()


        idGrupo=zapatilla.grupoPerteneciente.id
        
        listaZapatillas = Zapatilla.objects.filter(
            grupoPerteneciente=zapatilla.grupoPerteneciente)
        


        return render(request, "zapatillasApp/registrarZapatilla.html", {"idGrupo": idGrupo, "zapatillas": listaZapatillas, 'marcas': listaMarcas})

    else:

        
        return render(request, "zapatillasApp/editarZapatilla.html", {'zapatilla':zapatilla,'marcas': listaMarcas})



# CRUD: de Marca
def crearMarca(request):

    if request.method == "POST":
       
        nombre = request.POST["nombre"]

        marcaNueva = Marca(nombre=nombre)
        marcaNueva.save()

        listaMarcas = Marca.objects.all()
        return render(request, "zapatillasApp/crearMarca.html", {'marcas': listaMarcas})

    else:
        
        listaMarcas = Marca.objects.all()
        return render(request, "zapatillasApp/crearMarca.html", {'marcas': listaMarcas})


def editarMarca(request,idMarca):

    if request.method == "POST":
        nombre = request.POST["nombre"]

        marca=Marca.objects.get(id=idMarca)
        marca.nombre=nombre
        marca.save()
        
        listaMarcas = Marca.objects.all()
        return render(request, "zapatillasApp/crearMarca.html", {'marcas': listaMarcas})

    else:
        
        marca=Marca.objects.get(id=idMarca)
        return render(request, "zapatillasApp/editarMarca.html", {'marca': marca})


def eliminarMarca(request,idMarca):
    marca=Marca.objects.get(id=idMarca)
    marca.delete()

    # listaMarcas = Marca.objects.all()
    # return render(request, "zapatillasApp/crearMarca.html", {'marcas': listaMarcas})
    return HttpResponseRedirect(reverse('CrearMarca'))

# Fin del Crud de MARCA



# GAAAAAAAAAAAAAAA
def getGa(request):
    return render(request, "zapatillasApp/ga.html")
