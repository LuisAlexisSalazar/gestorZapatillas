from django.db import models

from zapatillasApp.models import Zapatilla
# Create your models here.


class Venta(models.Model):
    fechaVenta = models.DateField()
    precioVenta = models.DecimalField(max_digits=5, decimal_places=2)
    tipoPago = models.CharField(max_length=20)

    zapatillaCorrespondiente=models.OneToOneField(Zapatilla,on_delete=models.CASCADE)