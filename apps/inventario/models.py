from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=255)
    contacto = models.CharField(max_length=255)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    sku = models.CharField(max_length=50, unique=True)
    stock = models.IntegerField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
