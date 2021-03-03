from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from zapatillasApp.models import Marca
from .models import Zapatilla, Venta
# Create your views here.


def recibirCodigo(request):

    if request.method == "POST":
        codigo = request.POST["codigo"]

        listaZapatillas = Zapatilla.objects.filter(
            codigo__contains=codigo, vendido=False).order_by('-grupoPerteneciente__fechaIngreso')
        # Equivalente: SELECT * from zapatillasApp_zapatilla WHERE codigo LIKE '%codigo% AND vendido=False'

        return render(request, "ventaApp/recibirCodigo.html", {'zapatillas': listaZapatillas})

    else:

        return render(request, "ventaApp/recibirCodigo.html")


def recibirCaracteristicas(request):
    listaMarcas = Marca.objects.all()

    if request.method == "POST":
        modelo = request.POST["modelo"]
        talla = request.POST["talla"]
        marcaId = request.POST["marca"]

        marca = Marca.objects.get(id=marcaId)

        listaZapatillas = Zapatilla.objects.filter(
            vendido=False, modelo__icontains=modelo, talla=talla, marcaPerteneciente=marca).order_by('-grupoPerteneciente__fechaIngreso')

        # Ordenar la consulta por otro modelo
        # print(listaZapatillas.query)

        # Para ver los tipos de filtros revisar https://docs.djangoproject.com/en/3.1/ref/models/querysets/
        # __gte : es greater than and equal >=

        # icontains: Es como usar ILIKE de SQL

        # __iexact: es para que no distinga entre matusculas y minusculas por ejemplo si consultamos con "beatles blog" puede coindicir con "Beatles Blog", "beatles blog", o "BeAtlES blOG".

        return render(request, "ventaApp/recibirCaracteristicas.html", {'zapatillas': listaZapatillas, 'marcas': listaMarcas})

    else:

        return render(request, "ventaApp/recibirCaracteristicas.html", {'marcas': listaMarcas})


def zapatillasGenerales(request):
    # Get solo debe retornar 1 solo objeto
    # listaZapatillas = Zapatilla.objects.filter(
    #     vendido=False).order_by('grupoPerteneciente__fechaIngreso')

    listaZapatillas = Zapatilla.objects.filter(
        vendido=False).order_by('-grupoPerteneciente__fechaIngreso')
    # El menos es para ordenar de manera descendente

    return render(request, "ventaApp/zapatillasGenerales.html", {'zapatillas': listaZapatillas})






# CRUD de Venta
def crearVenta(request, idZapatilla):

    if request.method == "POST":

        fechaVenta = request.POST["fechaVenta"]
        precioVenta = request.POST["precioVenta"]
        tipoPago = request.POST["tipoPago"]

        zapatilla = Zapatilla.objects.get(id=idZapatilla)
        zapatilla.vendido = True
        zapatilla.save()

        ventaNueva = Venta(fechaVenta=fechaVenta, precioVenta=precioVenta,
                           tipoPago=tipoPago, zapatillaCorrespondiente=zapatilla)

        ventaNueva.save()

        return HttpResponseRedirect(reverse('Kardex'))

    else:

        zapatilla = Zapatilla.objects.get(id=idZapatilla)

        gananciaEsperada = zapatilla.precioSugerido-zapatilla.precioCompra

        return render(request, "ventaApp/registrarVenta.html", {'zapatilla': zapatilla, 'ganaciaEsperada': gananciaEsperada})


def eliminarVenta(request,idVenta):
    venta=Venta.objects.get(id=idVenta)

    zapatilla=venta.zapatillaCorrespondiente
    zapatilla.vendido=False
    zapatilla.save()
    
    venta.delete()
    
    return HttpResponseRedirect(reverse('Kardex'))


def editarVenta(request,idVenta):
    venta=Venta.objects.get(id=idVenta)

    if request.method == "POST":
        fechaVenta = request.POST["fechaVenta"]
        precioVenta = request.POST["precioVenta"]
        tipoPago = request.POST["tipoPago"]

        venta.fechaVenta=fechaVenta
        venta.precioVenta=precioVenta
        venta.tipoPago=tipoPago

        venta.save()


        return HttpResponseRedirect(reverse('Kardex'))

    else:
        
        zapatilla=venta.zapatillaCorrespondiente
        gananciaEsperada = zapatilla.precioSugerido-zapatilla.precioCompra

        return render(request, "ventaApp/editarVenta.html",{'zapatilla':zapatilla,'venta':venta,'ganaciaEsperada': gananciaEsperada})
