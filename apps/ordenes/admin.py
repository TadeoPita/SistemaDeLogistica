from django.contrib import admin
from .models import Orden, DetalleOrden

class DetalleOrdenInline(admin.TabularInline):
    model = DetalleOrden
    extra = 1
    autocomplete_fields = ('producto',)

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha_creacion', 'estado', 'codigo_seguimiento')
    search_fields = ('id', 'cliente__nombre', 'cliente__apellido', 'codigo_seguimiento')
    list_filter = ('estado', 'fecha_creacion')
    ordering = ('-fecha_creacion',)
    inlines = [DetalleOrdenInline]
    date_hierarchy = 'fecha_creacion'
    autocomplete_fields = ('cliente',)
    list_per_page = 25

@admin.register(DetalleOrden)
class DetalleOrdenAdmin(admin.ModelAdmin):
    list_display = ('orden', 'producto', 'cantidad', 'precio_unitario')
    search_fields = ('orden__id', 'producto__nombre')
    list_filter = ('producto',)
    ordering = ('orden',)
    autocomplete_fields = ('orden', 'producto')
    list_per_page = 25
