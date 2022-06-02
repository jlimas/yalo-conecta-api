from django.shortcuts import render

from .models import Boleto


def index(request):
    boletos = Boleto.objects.order_by("-fecha_compra")
    return render(request, "boletos.html", {"boletos": boletos})
