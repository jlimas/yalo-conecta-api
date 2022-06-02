from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views as authtoken_views

from api import views

router = routers.DefaultRouter()

router.register(r"usuarios", views.UsuarioViewSet)
router.register(r"partidos", views.PartidoViewSet)
router.register(r"boletos", views.BoletoViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("login/", authtoken_views.obtain_auth_token),
]
