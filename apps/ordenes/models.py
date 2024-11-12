from django.db import models
from apps.clientes.models import Cliente
from apps.inventario.models import Producto
import uuid


class Orden(models.Model):
    ESTADOS = [
        ('Pendiente', 'Pendiente'),
        ('Procesando', 'Procesando'),
        ('Completada', 'Completada'),
    ]
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=25, choices=ESTADOS, default='Pendiente')
    codigo_seguimiento = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"Orden {self.id} - {self.cliente}"


class DetalleOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_final = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def subtotal(self):
        return self.cantidad * self.precio_final
