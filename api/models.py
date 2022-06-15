from datetime import datetime

from django.conf import settings
from django.db import models


class Usuario(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=100)
    tenant = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=True
    )

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
    fecha_compra = models.DateTimeField(auto_now_add=True)
    tenant = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False, null=True
    )

    def __str__(self):
        return f"Boleto {self.usuario} Partido: {self.partido}"
