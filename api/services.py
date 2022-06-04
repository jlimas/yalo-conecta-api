import shortuuid

from api.models import Boleto


def process_payment(*, boleto: Boleto):
    boleto.pagado = True
    boleto.save()

    return {"pagoId": shortuuid.uuid()}
