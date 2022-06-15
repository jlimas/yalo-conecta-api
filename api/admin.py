from django.contrib import admin

from api import models


@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_filter = ("tenant",)
    list_display = ("id", "nombre", "tenant")


@admin.register(models.Partido)
class PartidoAdmin(admin.ModelAdmin):
    ordering = ("id",)
    list_filter = ("grupo", "estadio")
    list_display = ("id", "grupo", "local", "visitante", "estadio", "fecha")


@admin.register(models.Boleto)
class BoletoAdmin(admin.ModelAdmin):
    list_filter = ("tenant",)
    list_display = ("id", "usuario", "partido", "pagado", "tenant")
