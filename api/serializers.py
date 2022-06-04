from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from api.models import Boleto, Partido, Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"


class PartidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partido
        fields = "__all__"


class BoletoSerializer(serializers.ModelSerializer):
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


class BoletoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleto
        fields = "__all__"
        depth = 1
