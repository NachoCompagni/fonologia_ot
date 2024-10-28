from django.db import models

class Restriccion(models.Model):
    nombre = models.CharField(max_length=100)
    peso = models.IntegerField()

    def __str__(self):
        return self.nombre

    def violada_por(self, candidato):
        # Aquí va la lógica que define cuándo se viola esta restricción
        pass
