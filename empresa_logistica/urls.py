from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('inventario/', include('apps.inventario.urls')),
    # path('ordenes/', include('apps.ordenes.urls')),
    # path('envios/', include('apps.envios.urls')),
    # path('clientes/', include('apps.clientes.urls')),
    path('seguimiento/', include('apps.seguimiento.urls')),
]