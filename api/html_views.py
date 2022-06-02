from django.shortcuts import render

from .models import Boleto


def index(request):
    return render(request, "index.html")


def boletos(request):
    boletos = Boleto.objects.order_by("-fecha_compra")
    return render(request, "boletos.html", {"boletos": boletos})
