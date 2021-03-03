from django.db import models

from proveedorApp.models import Proveedor

# Create your models here.


class Grupo(models.Model):

    fechaIngreso = models.DateField()
    # creador = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    creador = models.ForeignKey(Proveedor, on_delete=models.CASCADE,related_name='grupo')
    def __str__(self):
        return 'fecha es %s' % (self.fechaIngreso)
