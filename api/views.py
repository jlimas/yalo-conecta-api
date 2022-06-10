from django.contrib.postgres.search import SearchVector
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from api.models import Boleto, Partido, Usuario
from api.serializers import (
    MatchSerializer,
    PaymentSerializer,
    TicketDetailSerializer,
    TicketSerializer,
    UserSerializer,
)
from api.services import get_teams_sorted_list, process_payment
from api.utils import ApiErrorsMixin


class MatchViewSet(ApiErrorsMixin, ModelViewSet):
    queryset = Partido.objects.all()
    serializer_class = MatchSerializer
    ordering = "fecha"

    def get_queryset(self):
        queryset = Partido.objects.all()
        pais = self.request.query_params.get("pais")
        if pais is not None:
            queryset = Partido.objects.annotate(
                pais=SearchVector("local", "visitante", config="spanish")
            )
            queryset = queryset.filter(pais=pais)
        return queryset


class UserViewSet(ApiErrorsMixin, ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer


class TicketViewSet(ApiErrorsMixin, ModelViewSet):
    queryset = Boleto.objects.all()
    ordering_fields = "__all__"
    ordering = "partido__fecha"
    search_fields = ("usuario__id",)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return TicketDetailSerializer
        return TicketSerializer


class PaymentViewSet(ApiErrorsMixin, ViewSet):
    def create(self, request):
        serializer = PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        boleto = serializer.validated_data["boleto"]  # type: ignore
        payment = process_payment(boleto=boleto)
        return Response(payment, status.HTTP_200_OK)


class TeamsViewSet(ApiErrorsMixin, ViewSet):
    def list(self, request):
        return Response(get_teams_sorted_list(), status.HTTP_200_OK)
