from django import forms
from .models import Orden, DetalleOrden
from django.forms import inlineformset_factory

class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = ['cliente', 'estado']

DetalleOrdenFormSet = inlineformset_factory(
    Orden,
    DetalleOrden,
    fields=('producto', 'cantidad', 'precio_unitario'),
    extra=1,
    can_delete=True
)
