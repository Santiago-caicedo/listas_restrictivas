# archivo: empresas/admin.py

from django.contrib import admin
from django_tenants.admin import TenantAdminMixin
from .models import Empresa, Domain

# Define cómo se mostrarán los Dominios 'dentro' de la página de Empresa
class DomainInline(admin.TabularInline):
    model = Domain
    max_num = 1 # Generalmente, cada inquilino tendrá solo un dominio principal

@admin.register(Empresa)
class EmpresaAdmin(TenantAdminMixin, admin.ModelAdmin):
    """
    Configuración personalizada para el modelo Empresa en el Admin.
    """
    list_display = ('nombre', 'schema_name', 'creado_en') # Campos a mostrar en la lista
    search_fields = ('nombre', 'schema_name') # Campos por los que se puede buscar
    inlines = [DomainInline] # Permite añadir/editar dominios aquí mismo

# Opcional: Registrar Domain por separado si quieres gestionarlos individualmente también
# @admin.register(Domain)
# class DomainAdmin(admin.ModelAdmin):
#     list_display = ('domain', 'tenant', 'is_primary')
#     search_fields = ('domain', 'tenant__nombre')