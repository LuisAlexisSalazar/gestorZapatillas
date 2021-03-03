from django.urls import path
from GenerarPDFApp import views

from django.contrib.auth.decorators import login_required
urlpatterns = [

    path('zapatillasVendedor',
         login_required(views.ListaZapatillas), name="PDFZapatillasVendedor"),
]
