from pyexpat import model
from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50, verbose_name='La Direccion')
    email = models.EmailField()
    telefono = models.CharField(max_length=7)

    def __str__(self):
        return 'El nombre es %s, la direccion es %s, el email es %s.' % (self.nombre, self.direccion, self.email)

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=7)
    precio = models.IntegerField() 

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
    #cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)