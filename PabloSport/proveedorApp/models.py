from django.db import models

# Create your models here.
#-*- coding: utf-8 -*-


class Proveedor(models.Model):
    
    nombre = models.CharField(max_length=15)


