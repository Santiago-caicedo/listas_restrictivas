# archivo: consultas/models.py

from django.db import models
from usuarios.models import Usuario

class Busqueda(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='busquedas')
    termino_buscado = models.CharField(max_length=100)
    fecha_busqueda = models.DateTimeField(auto_now_add=True)
    encontro_resultados = models.BooleanField(default=False)
    genero_alerta = models.BooleanField(default=False)

    def __str__(self):
        return f"Búsqueda de '{self.termino_buscado}' por {self.usuario.username}"

class Resultado(models.Model):
    busqueda = models.ForeignKey(Busqueda, related_name='resultados', on_delete=models.CASCADE)

    # Campos basados en la respuesta del API que vimos en el manual
    nombre_completo = models.CharField(max_length=255, null=True, blank=True)
    identificacion = models.CharField(max_length=50, null=True, blank=True)
    tipo_lista = models.CharField(max_length=100, null=True, blank=True)
    origen_lista = models.CharField(max_length=100, null=True, blank=True)
    relacionado_con = models.TextField(null=True, blank=True)
    fuente = models.CharField(max_length=255, null=True, blank=True)
    es_restrictiva = models.BooleanField(default=False)
    # Puedes añadir más campos del API si los necesitas

    def __str__(self):
        return f"Resultado para {self.nombre_completo}"