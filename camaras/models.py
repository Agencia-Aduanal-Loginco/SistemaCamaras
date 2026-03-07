from django.db import models

class Camara(models.Model):
    empresa = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    serie = models.CharField(max_length=100)
    ip = models.GenericIPAddressField()
    mac = models.CharField(max_length=17)

    def __str__(self):
        return self.nombre