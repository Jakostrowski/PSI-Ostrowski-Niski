from django.urls import include,path
from . import views

from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('test',KlientViewSet)
router.register('wizyta',WizytaViewSet)
router.register('pracownicy',PracownikViewSet)
router.register('uslugi',UslugaViewSet)
urlpatterns = [
    path("", views.default, name="default"),
    path('', include(router.urls)),
    path('api-auth/',include('rest_framework.urls'))
]