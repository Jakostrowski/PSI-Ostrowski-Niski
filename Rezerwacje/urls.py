from django.urls import include,path
from . import views
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('wizyta',WizytaViewSet)
router.register('pracownicy',PracownikViewSet,basename='pracownicy')
router.register('uslugi',UslugaViewSet,basename='uslugi')
router.register('klienci',KlientViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('',views.ApiRoot.as_view()),
    path('api-auth/',include('rest_framework.urls')),
    path('uslugi/',views.UslugaList.as_view(),name=views.UslugaList.name),
    path('uslugi/<str:pk>',views.UslugaDetail.as_view(),name=views.UslugaDetail.name),
    path('klienci/',views.KlientList.as_view(),name=views.KlientList.name),
    path('klienci/<str:pk>',views.KlientDetail.as_view(),name=views.KlientDetail.name),
    path('pracownicy/',views.PracownikList.as_view(),name=views.PracownikList.name),
    path('pracownicy/<int:pk>',views.PracownikDetail.as_view(),name=views.PracownikDetail.name),
]