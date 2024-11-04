from django.db import models

# Create your models here.
from django.db import models

class Area(models.Model):
    nombre = models.CharField(max_length=100)

class TipoParadero(models.Model):
    nombre = models.CharField(max_length=100)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

class Tarea(models.Model):
    nombre = models.CharField(max_length=100)

class Material(models.Model):
    nombre = models.CharField(max_length=100)


class Seleccion(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    tipo_paradero = models.ForeignKey(TipoParadero, on_delete=models.CASCADE)
    tareas = models.ManyToManyField(Tarea)
    materiales = models.ManyToManyField(Material)
    direccion = models.CharField(max_length=255)
    comuna = models.CharField(max_length=100)
    tiempo_estimado = models.CharField(max_length=50)
    ceco = models.CharField(max_length=100)
    jefe_proyecto = models.CharField(max_length=100)
    supervisor = models.CharField(max_length=100)
    cliente = models.CharField(max_length=100)
    otros = models.CharField(max_length=255, blank=True)
    observacion = models.TextField(blank=True)

    def __str__(self):
        return f"Seleccion de {self.area} - {self.tipo_paradero} para {self.cliente}"
