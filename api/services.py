import io

import shortuuid
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import cm
from reportlab.pdfbase.pdfmetrics import registerFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

from api.models import Boleto, Partido
from yalo.settings import BASE_DIR


def process_payment(*, boleto: Boleto):
    boleto.pagado = True
    boleto.save()

    return {"pagoId": shortuuid.uuid()}


def get_teams_sorted_list():
    equipos = set()
    for partido in Partido.objects.all():
        equipos.add(partido.local)
        equipos.add(partido.visitante)
    return sorted(equipos)


def generate_pdf_ticket(*, boleto: Boleto):
    font = "Lato"
    font_bold = font + "-Bold"

    registerFont(TTFont(font, BASE_DIR / "assets/Lato-Regular.ttf"))
    registerFont(TTFont(font_bold, BASE_DIR / "assets/Lato-Bold.ttf"))

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=letter)

    x_center = (21.59 / 2) * cm

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawImage(BASE_DIR / "assets/qatar.jpg", 2 * cm, 23 * cm, width=280, height=120)
    p.drawImage(BASE_DIR / "assets/yalo.png", 13 * cm, 23.5 * cm, width=200, height=90)

    match_y = 22 * cm
    p.setFont(font, 35)
    p.drawCentredString(x_center, match_y, text=f"Grupo {boleto.partido.grupo}")

    # Estadio
    p.setFont(font_bold, 30)
    p.drawCentredString(x_center, match_y - (2 * cm), text=f"{boleto.partido.estadio}")

    p.setFont(font, 40)
    p.drawCentredString(x_center, match_y - (4 * cm), text=str(boleto.partido))

    p.setFont(font, 20)
    p.drawCentredString(
        x_center,
        match_y - (5 * cm),
        text=f"{boleto.partido.fecha.strftime('%d %b, %Y %I:%M %p')}",
    )

    # Fecha de Compra
    p.setFont(font_bold, 20)
    p.drawCentredString(
        x_center,
        15 * cm,
        text=f"Fecha Compra",
    )
    p.setFont(font, 20)
    p.drawCentredString(
        x_center,
        14 * cm,
        text=f"{boleto.fecha_compra.strftime('%d %b, %Y %I:%M %p')}",
    )

    # Estatus de Pago
    p.setFont(font_bold, 30)
    if boleto.pagado:
        p.setFillColorRGB(0, 255, 0)
        p.drawCentredString(x_center, 12 * cm, text=f"Pagado")
    else:
        p.setFillColorRGB(255, 0, 0)
        p.drawCentredString(x_center, 12 * cm, text=f"Pago Pendiente")

    p.setFillColorRGB(0, 0, 0)
    # Usuario
    p.setFont(font_bold, 30)
    p.drawCentredString(
        x_center,
        10 * cm,
        text=f"{boleto.usuario.nombre}",
    )
    p.setFont(font, 25)
    p.drawCentredString(
        x_center,
        8 * cm,
        text=f"{boleto.usuario.id}",
    )

    p.setFont(font_bold, 100)
    p.drawCentredString(
        x_center,
        3 * cm,
        text=f"#{boleto.id}",  # type: ignore
    )

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)

    return buffer
