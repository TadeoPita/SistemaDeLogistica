from django.contrib import admin
from .models import Cliente, Direccion

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono')
    search_fields = ('nombre', 'apellido', 'email', 'dni')
    list_filter = ('direccion__ciudad',)

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('calle', 'numero', 'ciudad', 'provincia')
    search_fields = ('calle', 'ciudad', 'provincia')
    list_filter = ('provincia',)
