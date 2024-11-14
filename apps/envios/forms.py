from django import forms
from .models import Envio

class EnvioForm(forms.ModelForm):
    class Meta:
        model = Envio
        fields = ['orden', 'estado', 'fecha_envio', 'fecha_entrega']
        widgets = {
            'fecha_envio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_entrega': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
