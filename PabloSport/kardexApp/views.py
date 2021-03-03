from django.shortcuts import render

from ventaApp.models import Venta, Zapatilla
from gruposApp.models import Grupo


from django.db.models import Sum

import datetime


from django.db.models import F

# Tipos de Kardex
def kardexGeneral(request):
    # SELECT "id", "fechaVenta", "precioVenta","tipoPago", "zapatillaCorrespondiente_id", 
    # CAST(("precioVenta" - "zapatillasApp_zapatilla"."precioCompra") AS NUMERIC) AS "ganancia",
    # CAST(("zapatillasApp_zapatilla"."precioSugerido" - "zapatillasApp_zapatilla"."precioCompra") AS NUMERIC) AS "gananciaEsperada" 
    #   FROM "ventaApp_venta" 
    #   INNER JOIN "zapatillasApp_zapatilla" 
    #   ON ("zapatillaCorrespondiente_id" = "zapatillasApp_zapatilla"."id")
    # ORDER BY "fechaVenta" DESC


    # 2° Forma manualamente mucho mas costoso pero practico
    # for venta in  registroVentas:
    #     ganacia = venta.precioVenta-venta.zapatillaCorrespondiente.precioCompra

    #     gananciaEsperada = venta.zapatillaCorrespondiente.precioSugerido-venta.zapatillaCorrespondiente.precioCompra

    #     venta.ganancia = ganacia
    #     venta.gananciaEsperada = gananciaEsperada

    # registroVentas = Venta.objects.annotate(ganancia=F(
    #     'precioVenta')-F('zapatillaCorrespondiente__precioCompra')).annotate(gananciaEsperada=F('zapatillaCorrespondiente__precioSugerido')-F('zapatillaCorrespondiente__precioCompra')).order_by('-fechaVenta')

    registroVentas = Venta.objects.annotate(ganancia=F(
        'precioVenta')-F('zapatillaCorrespondiente__precioCompra')).annotate(gananciaEsperada=F('zapatillaCorrespondiente__precioSugerido')-F('zapatillaCorrespondiente__precioCompra')).order_by('-fechaVenta')
    
    # Aggregate siempre devuelve un diccionario
    diccionario=registroVentas.aggregate(ganaciaTotal=Sum('ganancia'))
    
    # print(registroVentas.get("ganaciaTotal"))


    return render(request, "kardexApp/kardexGeneral.html", {'ventas': registroVentas,'ganaciaTotal':diccionario.get('ganaciaTotal')})

    
def kardexRango(request):
    if request.method == "POST":

        inicio = request.POST['inicio']
        fin = request.POST['fin']

        # registroVentas = Venta.objects.filter(fechaVenta__range=[inicio,fin])

        registroVentas = Venta.objects.filter(fechaVenta__range=[inicio,fin]).annotate(ganancia=F(
        'precioVenta')-F('zapatillaCorrespondiente__precioCompra')).annotate(gananciaEsperada=F('zapatillaCorrespondiente__precioSugerido')-F('zapatillaCorrespondiente__precioCompra')).order_by('-fechaVenta')

        diccionario=registroVentas.aggregate(ganaciaTotal=Sum('ganancia'))

        return render(request, "kardexApp/kardexRango.html", {'ventas': registroVentas,'ganaciaTotal':diccionario.get('ganaciaTotal')})

    else:
        return render(request, "kardexApp/kardexRango.html")


def kardexHoy(request):

    today = datetime.datetime.now()
    
    registroVentas = Venta.objects.filter(fechaVenta__range=[today,today]).annotate(ganancia=F(
        'precioVenta')-F('zapatillaCorrespondiente__precioCompra')).annotate(gananciaEsperada=F('zapatillaCorrespondiente__precioSugerido')-F('zapatillaCorrespondiente__precioCompra')).order_by('-fechaVenta')

    diccionario=registroVentas.aggregate(ganaciaTotal=Sum('ganancia'))
    
    return render(request, "kardexApp/kardexHoy.html", {'ventas': registroVentas,'ganaciaTotal':diccionario.get('ganaciaTotal')})


def kardexModelo(request):
    if request.method == "POST":

        modelo = request.POST['modelo']


        # registroVentas = Venta.objects.filter(zapatillaCorrespondiente__modelo__icontains=modelo).annotate(ganancia=F(
        # 'precioVenta')-F('zapatillaCorrespondiente__precioCompra')).annotate(gananciaEsperada=F('zapatillaCorrespondiente__precioSugerido')-F('zapatillaCorrespondiente__precioCompra')).order_by('-fechaVenta')
        
        registroVentas = Venta.objects.filter(zapatillaCorrespondiente__modelo__icontains=modelo).annotate(ganancia=F(
        'precioVenta')-F('zapatillaCorrespondiente__precioCompra')).annotate(gananciaEsperada=F('zapatillaCorrespondiente__precioSugerido')-F('zapatillaCorrespondiente__precioCompra')).order_by('-fechaVenta')


        diccionario=registroVentas.aggregate(ganaciaTotal=Sum('ganancia'))

        return render(request, "kardexApp/kardexModelo.html", {'ventas': registroVentas,'ganaciaTotal':diccionario.get('ganaciaTotal')})

    else:
        return render(request, "kardexApp/kardexModelo.html")


