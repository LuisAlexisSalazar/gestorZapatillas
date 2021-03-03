from django.db import models


from gruposApp.models import Grupo

class Boleta(models.Model):

    codigoBoleta = models.CharField(max_length=9)
    precio = models.DecimalField(max_digits = 6, decimal_places = 2)

    GrupoPerteneciente = models.ForeignKey(Grupo, on_delete=models.PROTECT)
