from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sillon(models.Model):
    def __str__(self):
        return f'Nombre: {self.nombre} - Alto: {self.medida_alto} - Ancho: {self.medida_ancho} - Materiales: {self.materiales} - Precio: {self.precio} - Imagen {self.imagen}'
    nombre = models.CharField(max_length=40)
    medida_alto = models.IntegerField()
    medida_ancho = models.IntegerField()
    materiales = models.CharField(max_length=40)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='sillones', null=True, blank = True)
    
class Espejo(models.Model):
    def __str__(self):
      return f'Nombre: {self.nombre} - Alto: {self.medida_alto} - Ancho: {self.medida_ancho} - Materiales: {self.materiales} - Precio: {self.precio} - Imagen {self.imagen}'
    nombre = models.CharField(max_length=40)
    medida_alto = models.IntegerField()
    medida_ancho = models.IntegerField()
    materiales = models.CharField(max_length=40)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='espejos', null=True, blank = True)

class Lampara(models.Model):
    def __str__(self):
      return f'Nombre: {self.nombre} - Alto: {self.medida_alto} - Ancho: {self.medida_ancho} - Materiales: {self.materiales} - Luz: {self.colorluz} - Precio: {self.precio} - Imagen {self.imagen}'
    nombre = models.CharField(max_length=40)
    medida_alto = models.IntegerField()
    medida_ancho = models.IntegerField()
    materiales = models.CharField(max_length=40)
    colorluz = models.CharField(max_length=40)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='lamparas', null=True, blank = True)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
