# usuarios/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    # Añadimos un campo para relacionar al usuario con su empresa
    # Lo hacemos opcional (null=True) para que el superusuario no necesite empresa
    empresa = models.ForeignKey(
        'empresas.Empresa', 
        related_name="usuarios", 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )