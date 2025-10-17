# archivo: gestor_listas/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # La ruta del admin ahora es la pública, para superusuarios
    path('admin/', admin.site.urls),

    # Añadimos una ruta "cuentas/" que manejará el login, logout, etc.
    path('cuentas/', include('usuarios.urls')), 
    
    # La ruta raíz la manejará nuestra app de consultas
    path('', include('consultas.urls')),
]