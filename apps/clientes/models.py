from django.db import models
from django.contrib.auth.models import User


class Direccion(models.Model):
    PROVINCIAS = [
        ('BA', 'Buenos Aires'),
        ('CABA', 'Ciudad Autónoma de Buenos Aires'),
        ('CT', 'Catamarca'),
        ('CC', 'Chaco'),
        ('CH', 'Chubut'),
        ('CB', 'Córdoba'),
        ('CR', 'Corrientes'),
        ('ER', 'Entre Ríos'),
        ('FO', 'Formosa'),
        ('JY', 'Jujuy'),
        ('LP', 'La Pampa'),
        ('LR', 'La Rioja'),
        ('MZ', 'Mendoza'),
        ('MI', 'Misiones'),
        ('NQ', 'Neuquén'),
        ('RN', 'Río Negro'),
        ('SA', 'Salta'),
        ('SJ', 'San Juan'),
        ('SL', 'San Luis'),
        ('SC', 'Santa Cruz'),
        ('SF', 'Santa Fe'),
        ('SE', 'Santiago del Estero'),
        ('TF', 'Tierra del Fuego'),
        ('TM', 'Tucumán'),
    ]

    CIUDADES = [
        ('BA', [
            ('La Plata', 'La Plata'),
            ('Mar del Plata', 'Mar del Plata'),
            ('Bahía Blanca', 'Bahía Blanca'),
            ('Tandil', 'Tandil'),
        ]),
        ('CABA', [
            ('Buenos Aires', 'Buenos Aires')
        ]),
        ('CB', [
            ('Córdoba', 'Córdoba'),
            ('Villa María', 'Villa María'),
            ('Río Cuarto', 'Río Cuarto'),
        ]),
        ('SF', [
            ('Santa Fe', 'Santa Fe'),
            ('Rosario', 'Rosario'),
            ('Rafaela', 'Rafaela'),
        ]),
        ('MZ', [
            ('Mendoza', 'Mendoza'),
            ('San Rafael', 'San Rafael'),
            ('Godoy Cruz', 'Godoy Cruz'),
        ]),
    ]

    calle = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    departamento = models.CharField(max_length=10, blank=True, null=True)
    ciudad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=25, choices=PROVINCIAS, null=True)
    codigo_postal = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.ciudad}, Depto: {self.departamento}"


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    dni = models.CharField(max_length=20, unique=True)
    direccion = models.ForeignKey(
        Direccion,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='clientes'
    )
    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
