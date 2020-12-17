from django.urls import include,path
from . import views
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('wizyta',WizytaViewSet)
router.register('pracownicy',PracownikViewSet)
router.register('uslugi',UslugaViewSet)
router.register('klienci',KlientViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('',views.ApiRoot.as_view()),
    path('api-auth/',include('rest_framework.urls'))
]