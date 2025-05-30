from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=150, unique=True)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    nombres = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre_usuario