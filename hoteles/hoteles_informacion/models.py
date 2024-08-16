from django.db import models

# Create your models here.


class Tipo_habitacion(models.Model):
    Id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tarifa = models.FloatField()
    cant_personas = models.IntegerField()
    disponibilidad = models.BooleanField(default=True)

class Hotel(models.Model):
    Id = models.AutoField(primary_key=True)
    sede = models.CharField(max_length=100)
    cant_habitaciones = models.IntegerField()
    cant_personas_sede = models.IntegerField()
    tipo_habitaciones = models.ManyToManyField(Tipo_habitacion)

class Habitacion(models.Model):
    Id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=False, blank=True)
    tipo_habitacion = models.ForeignKey(Tipo_habitacion, on_delete=models.CASCADE, null = False, blank=True)


