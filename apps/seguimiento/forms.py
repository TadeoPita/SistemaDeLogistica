from django import forms

class SeguimientoForm(forms.Form):
    codigo_seguimiento = forms.UUIDField(label='Código de Seguimiento')
