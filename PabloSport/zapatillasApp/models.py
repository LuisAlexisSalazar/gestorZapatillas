from django.db import models

from gruposApp.models import Grupo, Proveedor
# Create your models here.


class Marca(models.Model):
    nombre = models.CharField(max_length=20)


class Zapatilla(models.Model):

    modelo = models.CharField(max_length=20)
    codigo = models.CharField(max_length=20)
    talla = models.DecimalField(max_digits=4, decimal_places=2)
    precioSugerido = models.DecimalField(max_digits=5, decimal_places=2)
    precioCompra = models.DecimalField(max_digits=5, decimal_places=2)

    # imagen = models.FileField()

    # dama, varón, infante o niño
    categoriaGenero = models.CharField(max_length=7)

    # deporte, caminar o vestir
    categoriaUso = models.CharField(max_length=7)
    descripcion = models.TextField(blank=True, default='')
    colorPrincipal = models.CharField(max_length=10)
    colorSecundario = models.TextField(blank=True, default='')

    vendido=models.BooleanField(default=False)

    marcaPerteneciente = models.ForeignKey(
        Marca, on_delete=models.CASCADE, null=True, blank=True)
    grupoPerteneciente = models.ForeignKey(Grupo, on_delete=models.CASCADE)
