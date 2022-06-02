from django.db import models
from datetime import datetime


class Usuario(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Partido(models.Model):
    local = models.CharField(max_length=100)
    visitante = models.CharField(max_length=100)
    estadio = models.CharField(max_length=100)
    grupo = models.CharField(max_length=100)
    fecha = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.local} vs {self.visitante}"


class Boleto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f"Boleto {self.usuario} Partido: {self.partido}"
