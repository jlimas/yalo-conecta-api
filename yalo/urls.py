from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from api import html_views
from api.views import BoletoViewSet, PartidoViewSet, UsuarioViewSet

admin.site.site_header = "Yalo Conecta Admin Panel"
admin.site.site_title = "Portal"
admin.site.index_title = "Yalo Conecta"

router = routers.DefaultRouter()

router.register(r"usuarios", UsuarioViewSet)
router.register(r"partidos", PartidoViewSet)
router.register(r"boletos", BoletoViewSet)


urlpatterns = [
    path("", html_views.index),
    path("boletos", html_views.boletos),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
