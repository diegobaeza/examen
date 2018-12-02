from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=70)
    costo_presupuesto = models.IntegerField(blank=True)
    costo_real = models.IntegerField(blank=True)
    tienda = models.ManyToManyField(Tienda)
    notas = models.TextField(max_length=200, blank=True)

class Tienda(models.Model):
    nombre = models.CharField(max_length=80)
    sucursal = models.CharField(max_length=80)
    direccion = models.CharField(max_length=80)
    ciudad = models.ManyToManyField(Ciudad, max_length=80)
    region = models.ManyToManyField(Region, max_length=80)

class Region(models.Model):
    nombre = models.CharField(max_length=80)

class Ciudad(models.Model):
    nombre = models.CharField(max_length=80)