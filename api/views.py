from rest_framework import viewsets

from api.models import Boleto, Partido, Usuario
from api.serializers import (
    BoletoDetailSerializer,
    BoletoSerializer,
    PartidoSerializer,
    UsuarioSerializer,
)
from api.utils import ApiErrorsMixin


class PartidoViewSet(ApiErrorsMixin, viewsets.ModelViewSet):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer
    ordering = "fecha"
    search_fields = ("local", "visitante")


class UsuarioViewSet(ApiErrorsMixin, viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class BoletoViewSet(ApiErrorsMixin, viewsets.ModelViewSet):
    queryset = Boleto.objects.all()
    ordering_fields = "__all__"
    ordering = "partido__fecha"
    search_fields = ("usuario__id",)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return BoletoDetailSerializer
        return BoletoSerializer
