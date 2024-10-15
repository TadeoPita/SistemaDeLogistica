from django.contrib import admin
from .models import Envio

@admin.register(Envio)
class EnvioAdmin(admin.ModelAdmin):
    list_display = ('orden', 'estado', 'fecha_envio', 'fecha_entrega')
    search_fields = ('orden__id', 'orden__codigo_seguimiento', 'orden__cliente__nombre', 'orden__cliente__apellido')
    list_filter = ('estado', 'fecha_envio', 'fecha_entrega')
    ordering = ('-fecha_envio',)
    autocomplete_fields = ('orden',)
    date_hierarchy = 'fecha_envio'
    list_per_page = 25
