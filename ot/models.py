from django.db import models

# Create your models here.

class PlanificacionMaterial(models.Model):
    area_trabajo = models.CharField(max_length=100)
    refugio_trabajo = models.CharField(max_length=100)
    tipos_tareas = models.CharField(max_length=100)
    materiales = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.area_trabajo} - {self.refugio_trabajo}"

class OTFormulario(models.Model):
    cliente = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    comuna = models.CharField(max_length=100)
    tiempo_estimado = models.DurationField()
    CECO = models.CharField(max_length=50)
    jefe_proyecto = models.CharField(max_length=100)
    supervisor = models.CharField(max_length=100)
    planificacion_material = models.ForeignKey(PlanificacionMaterial, on_delete=models.CASCADE)
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"OT {self.id} - {self.cliente} - {self.direccion}"
