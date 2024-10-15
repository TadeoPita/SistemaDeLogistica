from django.contrib import admin
from .models import Producto, Empresa

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'sku', 'stock', 'empresa')
    search_fields = ('nombre', 'sku', 'empresa__nombre')
    list_filter = ('empresa',)
    ordering = ('nombre',)
    autocomplete_fields = ('empresa',)
    list_per_page = 25

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'contacto', 'email', 'telefono')
    search_fields = ('nombre', 'contacto', 'email')
    ordering = ('nombre',)
    list_per_page = 25
