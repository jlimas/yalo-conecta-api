import json
import time

from time import mktime
from datetime import datetime
from django.core.management.base import BaseCommand
from api.models import Partido


class Command(BaseCommand):
    def handle(self, *args, **options):
        Partido.objects.all().delete()
        with open("fixtures/matches.json") as matches_json:
            matches = json.load(matches_json)
            for match in matches:
                id = match["MatchNumber"]
                local = match["HomeTeam"]
                visitante = match["AwayTeam"]
                estadio = match["Location"]

                fixed_datetime = match["DateUtc"][:-1]
                struct_datetime = time.strptime(fixed_datetime, "%Y-%m-%d %H:%M:%S")
                fecha = datetime.fromtimestamp(mktime(struct_datetime))

                print("Creating Match", id, fecha, local, visitante, estadio)

                Partido.objects.create(
                    id=id,
                    local=local,
                    visitante=visitante,
                    estadio=estadio,
                    fecha=fecha,
                )
