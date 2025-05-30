from django.db import models
from applications.proyectos.models import Proyecto

class Tarea(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    estado = models.CharField(max_length=50)
    prioridad = models.IntegerField()
    fecha_entrega = models.DateField()
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    esta_completada = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo