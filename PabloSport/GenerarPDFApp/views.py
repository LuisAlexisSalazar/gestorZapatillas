from django.shortcuts import render ,HttpResponse


from zapatillasApp.models import Zapatilla

# Investigar
from django.views.generic import ListView,View
from .utils import render_to_pdf

def ListaZapatillas(request):
    
    if request.method == "GET":
        listaZapatillas=Zapatilla.objects.filter(vendido=False)
      
        data={'zapatillas':listaZapatillas}

        pdf=render_to_pdf("GenerarPDFApp/zapatillasVendedor.html",data)
        return HttpResponse(pdf,content_type='application/pdf')

    return render(request,"GenerarPDFApp/zapatillasVendedor.html",{'zapatillas':listaZapatillas})

