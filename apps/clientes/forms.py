from django import forms
from .models import Cliente, Direccion

class ClienteForm(forms.ModelForm):
    calle = forms.CharField(max_length=255)
    numero = forms.CharField(max_length=10)
    departamento = forms.CharField(max_length=10, required=False)
    ciudad = forms.ChoiceField(choices=Direccion.CIUDADES)
    provincia = forms.ChoiceField(choices=Direccion.PROVINCIAS)
    codigo_postal = forms.CharField(max_length=10)

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono', 'dni']
