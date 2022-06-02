from rest_framework import viewsets
from .models import Partido, Usuario, Boleto
from .serializers import (
    PartidoSerializer,
    UsuarioSerializer,
    BoletoSerializer,
    BoletoDetailSerializer,
)
from .utils import ApiErrorsMixin


class PartidoViewSet(ApiErrorsMixin, viewsets.ModelViewSet):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer
    ordering = "fecha"
    search_fields = ("local", "visitante")


class UsuarioViewSet(viewsets.ModelViewSet):
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
