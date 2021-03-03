from django.urls import path
from verZapatillasApp import views

from django.contrib.auth.decorators import login_required

urlpatterns = [


    path('verZapatillasGeneral',
         login_required(views.verZapatillasGeneral), name="VerZapatillasGeneral"),
    path('verZapatillasCodigo',
         login_required(views.verZapatillasCodigo), name="VerZapatillasCodigo"),
    path('verZapatillasModelo',
         login_required(views.verZapatillasModelo), name="VerZapatillasModelo"),
    path('verZapatillasTalla',
         login_required(views.verZapatillasTalla), name="VerZapatillasTalla"),

    path('verZapatillasMarca',
         login_required(views.verZapatillasMarca), name="VerZapatillasMarca"),


]
