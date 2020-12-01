from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets

from .serializers import KlientSerializer,WizytaSerializer,PracownikSerializer,UslugaSerializer
from .models import Klient,Wizyta,Pracownik,Usluga
# Create your views here.


def default(request):
    return HttpResponse("Hello, WORLD")
class KlientViewSet(viewsets.ModelViewSet):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
class WizytaViewSet(viewsets.ModelViewSet):
    queryset= Wizyta.objects.all()
    serializer_class= WizytaSerializer
class PracownikViewSet(viewsets.ModelViewSet):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer
class UslugaViewSet(viewsets.ModelViewSet):
    queryset = Usluga.objects.all()
    serializer_class = UslugaSerializer