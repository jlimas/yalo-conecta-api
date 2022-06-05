import shortuuid
from django.http.response import FileResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework import status

from api.services import generate_pdf_ticket

from .models import Boleto


def index(request):
    return render(request, "index.html")


def boletos(request):
    boletos = Boleto.objects.order_by("-fecha_compra")
    return render(request, "boletos.html", {"boletos": boletos})


@csrf_exempt
@require_http_methods(["GET"])
def generar_boleto_pdf(request, boleto_id):
    try:
        boleto = Boleto.objects.get(pk=boleto_id)
        file = generate_pdf_ticket(boleto=boleto)
        return FileResponse(
            file, as_attachment=True, filename=f"{shortuuid.uuid()}.pdf"
        )
    except Boleto.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
