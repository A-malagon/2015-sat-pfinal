from django.db import models

# Create your models here.

class Contenidos(models.Model):
    titulo = models.CharField(max_length=128)
    tipo = models.CharField(max_length=128)
    precio = models.CharField(max_length=128)
    fecha = models.CharField(max_length=128)
    hora = models.CharField(max_length=128)
    fechaFin = models.CharField(max_length=128)
    eventoLargo = models.IntegerField()
    informacion = models.TextField()

class Usuario(models.Model):
    titulo = models.CharField(max_length=128)
    nombre = models.CharField(max_length=128)
    comentario = models.CharField(max_length=128)
    actividades = models.ManyToManyField(Contenidos, through='Membership')

class Membership(models.Model):
    contenido = models.ForeignKey(Contenidos)
    usuario = models.ForeignKey(Usuario)
    fechaEleccion = models.CharField(max_length=128)

class FechaActualizacion(models.Model):
    fecha = models.CharField(max_length=128)
