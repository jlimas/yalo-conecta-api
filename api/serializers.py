from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework.validators import UniqueTogetherValidator

from api.models import Boleto, Partido, Usuario


class UserSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"


class MatchSerializer(ModelSerializer):
    class Meta:
        model = Partido
        fields = "__all__"


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Boleto
        fields = "__all__"
        validators = [
            UniqueTogetherValidator(
                queryset=Boleto.objects.all(),
                message="este usuario ya tiene boleto para este juego",
                fields=("partido", "usuario"),
            )
        ]


class TicketDetailSerializer(ModelSerializer):
    class Meta:
        model = Boleto
        fields = "__all__"
        depth = 1


class PaymentSerializer(Serializer):
    usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    boleto = serializers.PrimaryKeyRelatedField(queryset=Boleto.objects.all())
    nip = serializers.CharField(required=True)
    tarjeta = serializers.CharField(required=True)

    def validate(self, data):
        if data["boleto"].pagado:
            raise ValidationError("Este boleto ya se encuentra pagado")
        if data["usuario"] != data["boleto"].usuario:
            raise ValidationError("Este usuario no es dueño de este boleto")
        if data["tarjeta"][-4:] != data["nip"]:
            raise ValidationError("El nip es invalido para esta tarjeta")
        return data
