from django.contrib import admin
from api import models


@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")


@admin.register(models.Partido)
class PartidoAdmin(admin.ModelAdmin):
    list_display = ("id", "local", "visitante", "estadio", "fecha")


@admin.register(models.Boleto)
class BoletoAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "partido")
