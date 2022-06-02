from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as authtoken_views

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
    path("admin/", admin.site.urls),
    path("login/", authtoken_views.obtain_auth_token),
    path("boletos", html_views.index),
    path("v1/", include(router.urls)),
]
