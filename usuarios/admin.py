# archivo: usuarios/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class CustomUserAdmin(UserAdmin):
    # Añadimos 'empresa' a los campos mostrados
    fieldsets = UserAdmin.fieldsets + (
        ('Información de la Empresa', {'fields': ('empresa',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información de la Empresa', {'fields': ('empresa',)}),
    )
    # Mostramos 'empresa' también en la lista de usuarios
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'empresa')
    list_filter = UserAdmin.list_filter + ('empresa',) # Permite filtrar por empresa

admin.site.register(Usuario, CustomUserAdmin)