from django import forms
from django.forms import inlineformset_factory
from .models import Orden, DetalleOrden

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['cliente', 'estado']

# Configuración del FormSet con extra=1 para un formulario adicional
DetalleOrdenFormSet = inlineformset_factory(
    Orden,
    DetalleOrden,
    fields=('producto', 'cantidad', 'precio_final'),
    extra=1,  # Permite agregar un producto adicional en la edición
    can_delete=True  # Permite eliminar productos
)
