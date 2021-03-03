from django.shortcuts import render

from ventaApp.models import Zapatilla, Venta
from zapatillasApp.models import Marca

from django.db.models import F, Sum
# Create your views here.


def verZapatillasGeneral(request):
    if request.method == "POST":

        # devuelve una lista de todas los chekbos que el usuario escogio
        seleccionLista = request.POST.getlist('seleccionOpcion')
        seleccion = seleccionLista[0]

        if seleccion == 'soloVendidas':

            registroVentas = Venta.objects.annotate(ganancia=F(
                'precioVenta')-F('zapatillaCorrespondiente__precioCompra')).annotate(gananciaEsperada=F('zapatillaCorrespondiente__precioSugerido')-F('zapatillaCorrespondiente__precioCompra')).order_by('-fechaVenta')

            diccionario = registroVentas.aggregate(
                ganaciaTotal=Sum('ganancia'))

            return render(request, "verZapatillasApp/verZapatillasGeneral.html", {'ventas': registroVentas, 'ganaciaTotal': diccionario.get('ganaciaTotal'), 'seleccion': seleccion})

        elif seleccion == 'soloNoVendidas':

            listaZapatillas = Zapatilla.objects.filter(
                vendido=False).order_by('-grupoPerteneciente__fechaIngreso')

            return render(request, "verZapatillasApp/verZapatillasGeneral.html", {'zapatillas': listaZapatillas, 'seleccion': seleccion})

        # # Ambas:Vendidas y no vendidas
        else:
            # Vendidas
            registroVentas = Venta.objects.annotate(ganancia=F(
                'precioVenta')-F('zapatillaCorrespondiente__precioCompra')).annotate(gananciaEsperada=F('zapatillaCorrespondiente__precioSugerido')-F('zapatillaCorrespondiente__precioCompra')).order_by('-fechaVenta')

            diccionario = registroVentas.aggregate(
                ganaciaTotal=Sum('ganancia'))

            # Zapatillas no vendidas
            listaZapatillas = Zapatilla.objects.filter(
                vendido=False).order_by('-grupoPerteneciente__fechaIngreso')

            return render(request, "verZapatillasApp/verZapatillasGeneral.html", {'zapatillas': listaZapatillas, 'seleccion': seleccion, 'ventas': registroVentas, 'ganaciaTotal': diccionario.get('ganaciaTotal')})

    else:
        return render(request, "verZapatillasApp/verZapatillasGeneral.html")


def verZapatillasCodigo(request):
    if request.method == "POST":

        # devuelve una lista de todas los chekbos que el usuario escogio
        seleccionLista = request.POST.getlist('seleccionOpcion')
        seleccion = seleccionLista[0]

        codigo = request.POST["codigo"]
        
        if seleccion == 'soloVendidas':

            registroVentas = Venta.objects.filter(zapatillaCorrespondiente__codigo__contains=codigo).annotate(ganancia=F(
                'precioVenta')-F('zapatillaCorrespondiente__precioCompra')).annotate(gananciaEsperada=F('zapatillaCorrespondiente__precioSugerido')-F('zapatillaCorrespondiente__precioCompra')).order_by('-fechaVenta')

            diccionario = registroVentas.aggregate(
                ganaciaTotal=Sum('ganancia'))

            return render(request, "verZapatillasApp/verZapatillasCodigo.html", {'ventas': registroVentas, 'ganaciaTotal': diccionario.get('ganaciaTotal'), 'seleccion': seleccion})

        elif seleccion == 'soloNoVendidas':

            listaZapatillas = Zapatilla.objects.filter(
                vendido=False, codigo__contains=codigo).order_by('-grupoPerteneciente__fechaIngreso')

            return render(request, "verZapatillasApp/verZapatillasCodigo.html", {'zapatillas': listaZapatillas, 'seleccion': seleccion})

        # # Ambas:Vendidas y no vendidas
        else:
            # Vendidas
            registroVentas = Venta.objects.filter(zapatillaCorrespondiente__codigo__contains=codigo).annotate(ganancia=F(
                'precioVenta')-F('zapatillaCorrespondiente__precioCompra')).annotate(gananciaEsperada=F('zapatillaCorrespondiente__precioSugerido')-F('zapatillaCorrespondiente__precioCompra')).order_by('-fechaVenta')

            diccionario=registroVentas.aggregate(ganaciaTotal=Sum('ganancia'))


            # Zapatillas no vendidas
            listaZapatillas = Zapatilla.objects.filter(vendido=False,codigo__contains=codigo).order_by('-grupoPerteneciente__fechaIngreso')
            

            return render(request, "verZapatillasApp/verZapatillasCodigo.html", {'zapatillas': listaZapatillas,'seleccion':seleccion,'ventas': registroVentas,'ganaciaTotal':diccionario.get('ganaciaTotal')})

            
    else:
        return render(request, "verZapatillasApp/verZapatillasCodigo.html")


def verZapatillasModelo(request):
    if request.method == "POST":

        # devuelve una lista de todas los chekbos que el usuario escogio
        seleccionLista = request.POST.getlist('seleccionOpcion')
        seleccion = seleccionLista[0]

        modelo = request.POST["modelo"]
        print(modelo)
        print(seleccion)

        if seleccion == 'soloVendidas':

            registroVentas = Venta.objects.filter(zapatillaCorrespondiente__modelo__icontains=modelo).annotate(ganancia=F(
                'precioVenta')-F('zapatillaCorrespondiente__precioCompra')).annotate(gananciaEsperada=F('zapatillaCorrespondiente__precioSugerido')-F('zapatillaCorrespondiente__precioCompra')).order_by('-fechaVenta')

            diccionario = registroVentas.aggregate(
                ganaciaTotal=Sum('ganancia'))

            return render(request, "verZapatillasApp/verZapatillasModelo.html", {'ventas': registroVentas, 'ganaciaTotal': diccionario.get('ganaciaTotal'), 'seleccion': seleccion})

        elif seleccion == 'soloNoVendidas':

            listaZapatillas = Zapatilla.objects.filter(
                vendido=False, modelo__contains=modelo).order_by('-grupoPerteneciente__fechaIngreso')

            return render(request, "verZapatillasApp/verZapatillasModelo.html", {'zapatillas': listaZapatillas, 'seleccion': seleccion})

        # # Ambas:Vendidas y no vendidas
        else:
            # Vendidas
            registroVentas = Venta.objects.filter(zapatillaCorrespondiente__modelo__icontains=modelo).annotate(ganancia=F(
                'precioVenta')-F('zapatillaCorrespondiente__precioCompra')).annotate(gananciaEsperada=F('zapatillaCorrespondiente__precioSugerido')-F('zapatillaCorrespondiente__precioCompra')).order_by('-fechaVenta')

            diccionario=registroVentas.aggregate(ganaciaTotal=Sum('ganancia'))


            # Zapatillas no vendidas
            listaZapatillas = Zapatilla.objects.filter(vendido=False,modelo__icontains=modelo).order_by('-grupoPerteneciente__fechaIngreso')
            

            return render(request, "verZapatillasApp/verZapatillasModelo.html", {'zapatillas': listaZapatillas,'seleccion':seleccion,'ventas': registroVentas,'ganaciaTotal':diccionario.get('ganaciaTotal')})

            
    else:
        return render(request, "verZapatillasApp/verZapatillasModelo.html")


def verZapatillasTalla(request):
    if request.method == "POST":

        # devuelve una lista de todas los chekbos que el usuario escogio
        seleccionLista = request.POST.getlist('seleccionOpcion')
        seleccion = seleccionLista[0]

        talla = request.POST["talla"]

        if seleccion == 'soloVendidas':

            registroVentas = Venta.objects.filter(zapatillaCorrespondiente__talla=talla).annotate(ganancia=F(
                'precioVenta')-F('zapatillaCorrespondiente__precioCompra')).annotate(gananciaEsperada=F('zapatillaCorrespondiente__precioSugerido')-F('zapatillaCorrespondiente__precioCompra')).order_by('-fechaVenta')

            diccionario = registroVentas.aggregate(
                ganaciaTotal=Sum('ganancia'))

            return render(request, "verZapatillasApp/verZapatillasTalla.html", {'ventas': registroVentas, 'ganaciaTotal': diccionario.get('ganaciaTotal'), 'seleccion': seleccion})

        elif seleccion == 'soloNoVendidas':

            listaZapatillas = Zapatilla.objects.filter(
                vendido=False, talla=talla).order_by('-grupoPerteneciente__fechaIngreso')

            return render(request, "verZapatillasApp/verZapatillasTalla.html", {'zapatillas': listaZapatillas, 'seleccion': seleccion})

        # # Ambas:Vendidas y no vendidas
        else:
            # Vendidas
            registroVentas = Venta.objects.filter(zapatillaCorrespondiente__talla=talla).annotate(ganancia=F(
                'precioVenta')-F('zapatillaCorrespondiente__precioCompra')).annotate(gananciaEsperada=F('zapatillaCorrespondiente__precioSugerido')-F('zapatillaCorrespondiente__precioCompra')).order_by('-fechaVenta')

            diccionario=registroVentas.aggregate(ganaciaTotal=Sum('ganancia'))


            # Zapatillas no vendidas
            listaZapatillas = Zapatilla.objects.filter(vendido=False,talla=talla).order_by('-grupoPerteneciente__fechaIngreso')
            

            return render(request, "verZapatillasApp/verZapatillasTalla.html", {'zapatillas': listaZapatillas,'seleccion':seleccion,'ventas': registroVentas,'ganaciaTotal':diccionario.get('ganaciaTotal')})

            
    else:
        return render(request, "verZapatillasApp/verZapatillasTalla.html")



def verZapatillasMarca(request):
    marcas=Marca.objects.all()

    if request.method == "POST":

        # devuelve una lista de todas los chekbos que el usuario escogio
        seleccionLista = request.POST.getlist('seleccionOpcion')
        seleccion = seleccionLista[0]

        marcaId = request.POST["marca"]

        marca=Marca.objects.get(id=marcaId)

        if seleccion == 'soloVendidas':

            registroVentas = Venta.objects.filter(zapatillaCorrespondiente__marcaPerteneciente=marca).annotate(ganancia=F(
                'precioVenta')-F('zapatillaCorrespondiente__precioCompra')).annotate(gananciaEsperada=F('zapatillaCorrespondiente__precioSugerido')-F('zapatillaCorrespondiente__precioCompra')).order_by('-fechaVenta')

            diccionario = registroVentas.aggregate(
                ganaciaTotal=Sum('ganancia'))

            return render(request, "verZapatillasApp/verZapatillasMarca.html", {'ventas': registroVentas, 'ganaciaTotal': diccionario.get('ganaciaTotal'), 'seleccion': seleccion,'marcas':marcas})

        elif seleccion == 'soloNoVendidas':

            listaZapatillas = Zapatilla.objects.filter(
                vendido=False, marcaPerteneciente=marca).order_by('-grupoPerteneciente__fechaIngreso')

            return render(request, "verZapatillasApp/verZapatillasMarca.html", {'zapatillas': listaZapatillas, 'seleccion': seleccion,'marcas':marcas})

        # # Ambas:Vendidas y no vendidas
        else:
            # Vendidas
            registroVentas = Venta.objects.filter(zapatillaCorrespondiente__marcaPerteneciente=marca).annotate(ganancia=F(
                'precioVenta')-F('zapatillaCorrespondiente__precioCompra')).annotate(gananciaEsperada=F('zapatillaCorrespondiente__precioSugerido')-F('zapatillaCorrespondiente__precioCompra')).order_by('-fechaVenta')

            diccionario=registroVentas.aggregate(ganaciaTotal=Sum('ganancia'))


            # Zapatillas no vendidas
            listaZapatillas = Zapatilla.objects.filter(vendido=False,marcaPerteneciente=marca).order_by('-grupoPerteneciente__fechaIngreso')
            

            return render(request, "verZapatillasApp/verZapatillasMarca.html", {'zapatillas': listaZapatillas,'seleccion':seleccion,'ventas': registroVentas,'ganaciaTotal':diccionario.get('ganaciaTotal'),'marcas':marcas})

            
    else:
        

        return render(request, "verZapatillasApp/verZapatillasMarca.html",{'marcas':marcas})
