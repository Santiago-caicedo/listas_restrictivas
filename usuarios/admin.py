# archivo: usuarios/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

# Creamos una clase de Admin personalizada que hereda de UserAdmin
class CustomUserAdmin(UserAdmin):
    # 'fieldsets' controla los campos que se muestran en la página de EDICIÓN de un usuario.
    # Copiamos los fieldsets originales de UserAdmin y le añadimos una nueva sección.
    fieldsets = UserAdmin.fieldsets + (
        ('Información de la Empresa', {'fields': ('empresa',)}),
    )

    # 'add_fieldsets' controla los campos para la página de CREACIÓN de un nuevo usuario.
    # Hacemos lo mismo: copiamos los originales y añadimos nuestra sección.
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información de la Empresa', {'fields': ('empresa',)}),
    )

# Finalmente, registramos nuestro modelo Usuario pero usando
# nuestra clase de configuración personalizada.
admin.site.register(Usuario, CustomUserAdmin)