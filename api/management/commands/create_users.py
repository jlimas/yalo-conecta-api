from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from rest_framework.authtoken.models import Token

from api.models import Partido


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("number_of_users", type=int, default=0)

    def handle(self, *args, **options):
        number_of_users = options["number_of_users"]
        for i in range(1, number_of_users + 1):
            user = User.objects.create_user(f"equipo{i}", f"equipo{i}@yalo.com", "y4l0")
            user.first_name = f"Equipo {i}"
            user.last_name = f"Yalo Conecta"
            user.save()
            token = Token.objects.create(user=user)
            print("Created User", user, "Token", token)
