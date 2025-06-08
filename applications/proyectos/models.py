from django.db import models
from applications.usuario.models import Usuario

class Proyecto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True)
    fecha_final = models.DateField()
    numero_integrantes = models.IntegerField()
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    esta_activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    proyecto = models.ForeignKey(Proyecto, related_name='tareas', on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=255)
    completada = models.BooleanField(default=False)
    creada_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion