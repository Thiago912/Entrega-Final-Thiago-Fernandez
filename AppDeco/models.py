from django.db import models

# Create your models here.
class Sillon(models.Model):
    nombre = models.CharField(max_length=40)
    medida_alto = models.IntegerField()
    medida_ancho = models.IntegerField()
    materiales = models.CharField(max_length=40)
    precio = models.IntegerField()
class Espejo(models.Model):
    nombre = models.CharField(max_length=40)
    medida_alto = models.IntegerField()
    medida_ancho = models.IntegerField()
    materiales = models.CharField(max_length=40)
    precio = models.IntegerField()

class Lampara(models.Model):
    nombre = models.CharField(max_length=40)
    medida_alto = models.IntegerField()
    medida_ancho = models.IntegerField()
    materiales = models.CharField(max_length=40)
    colorluz = models.CharField(max_length=40)
    precio = models.IntegerField()
