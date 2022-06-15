from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api import html_views
from api.views import (
    MatchViewSet,
    PaymentViewSet,
    TeamsViewSet,
    TicketViewSet,
    UserViewSet,
)

admin.site.site_header = "Yalo Conecta Admin Panel"
admin.site.site_title = "Portal"
admin.site.index_title = "Yalo Conecta"

router = routers.DefaultRouter()

router.register(r"usuarios", UserViewSet, basename="users")
router.register(r"partidos", MatchViewSet, basename="matches")
router.register(r"boletos", TicketViewSet, basename="tickets")
router.register(r"pagos", PaymentViewSet, basename="payments")
router.register(r"equipos", TeamsViewSet, basename="teams")


urlpatterns = [
    path("", html_views.index),
    path("boletos", html_views.boletos, name="boletos"),
    path("equipos", html_views.equipos, name="equipos"),
    path("documentacion", html_views.documentacion, name="documentacion"),
    path("studio", html_views.studio, name="studio"),
    path("recursos", html_views.recursos, name="recursos"),
    path("caso-de-uso", html_views.caso_de_uso, name="caso-de-uso"),
    path("boleto/<int:boleto_id>/pdf", html_views.generar_boleto_pdf),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
