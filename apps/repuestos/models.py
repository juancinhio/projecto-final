from django.db import models

# Create your models here.

class Afinacion(models.Model):
    detalle_afinacion = models.TextField(blank=True, null=True)
    precio = models.BigIntegerField()

class Frenos(models.Model):    
    detalle_frenos = models.TextField(blank=True, null=True)
    precio = models.BigIntegerField()
class Suspencion(models.Model):
    detalle_suspencion = models.TextField(blank=True, null=True)
    precio = models.BigIntegerField()

class Service(models.Model):
    detalle_service = models.TextField(blank=True, null=True)
    precio = models.BigIntegerField()

class Embrague(models.Model):
    detalle_embrague = models.TextField(blank=True, null=True)
    precio = models.BigIntegerField()

class Distribucion(models.Model):
    detalle_distribucion = models.TextField(blank=True, null=True)
    precio = models.BigIntegerField()

class Circuito_Refrigerante(models.Model):
    detalle_circuito_refrigerante = models.TextField(blank=True, null=True)
    precio = models.BigIntegerField()

class Electricidad(models.Model):
    detalle_electricidad = models.TextField(blank=True, null=True)
    precio = models.BigIntegerField()

class Motor(models.Model):
    detalle_motor = models.TextField(blank=True, null=True)
    precio = models.BigIntegerField()

class Otros(models.Model):
    detalle_otros = models.TextField(blank=True, null=True)
    precio = models.BigIntegerField()
    
