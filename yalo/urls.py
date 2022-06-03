from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api import views
from api import html_views

admin.site.site_header = "Yalo Conecta Admin Panel"
admin.site.site_title = "Portal"
admin.site.index_title = "Yalo Conecta"

router = routers.DefaultRouter()

router.register(r"usuarios", views.UsuarioViewSet)
router.register(r"partidos", views.PartidoViewSet)
router.register(r"boletos", views.BoletoViewSet)


urlpatterns = [
    path("", html_views.index),
    path("boletos", html_views.boletos),
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
