from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length= 50)
    precio = models.IntegerField()
    categoria = models.CharField(max_length= 35, default='General')
    stock = models.IntegerField()
    descripcion = models.CharField(max_length= 500)
    imagen = models.CharField(max_length= 200)

    def __str__(self):
        return self.nombre
