from django.urls import include,path
from . import views

from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
<<<<<<< HEAD
router.register('wizyta',WizytaViewSet)
router.register('pracownicy',PracownikViewSet)
router.register('uslugi',UslugaViewSet)
router.register('klienci',KlientViewSet)
urlpatterns = [
    path("", views.default, name="default"),
    path('', include(router.urls)),
    path('klienci2/',views.KlientList.as_view()),
    path('klienci2/<int:pk>/',views.KlientDetail.as_view()),
    path('klienci2/<int:pk>',views.KlientDetail.as_view()),
    path('uslugi2',views.UslugaList.as_view()),
    path('uslugi2/<int:pk>',views.UslugaDetail.as_view()),
    path('api-auth/',include('rest_framework.urls'))

=======
router.register('test',KlientViewSet)
router.register('wizyta',WizytaViewSet)
router.register('pracownicy',PracownikViewSet)
router.register('uslugi',UslugaViewSet)
urlpatterns = [
    path("", views.default, name="default"),
    path('', include(router.urls)),
    path('api-auth/',include('rest_framework.urls'))
>>>>>>> e1207a4b1d513de65d2171ec9a3d61c8761ac25f
]