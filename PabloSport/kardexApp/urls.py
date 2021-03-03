from django.urls import path
from kardexApp import views

from django.contrib.auth.decorators import login_required

urlpatterns = [


    path('kardex',login_required(views.kardexGeneral), name="Kardex"),
    path('kardexRango',login_required(views.kardexRango), name="KardexRango"),
    path('kardexHoy',login_required(views.kardexHoy), name="KardexHoy"),
    path('kardexModelo',login_required(views.kardexModelo), name="KardexModelo"),
    

]
