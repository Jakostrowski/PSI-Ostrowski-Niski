from django.shortcuts import render
from django.http import HttpResponse,Http404
from rest_framework import viewsets,generics,status
from rest_framework.views import APIView
from .serializers import KlientSerializer,WizytaSerializer,PracownikSerializer,UslugaSerializer
from .models import Klient,Wizyta,Pracownik,Usluga
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django_filters import NumberFilter, FilterSet, DateTimeFilter
# Create your views here.

def default(request):
    return HttpResponse("Hello, WORLD")
class KlientViewSet(viewsets.ModelViewSet):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
    filter_fields = ['nazwisko',]
    search_fields = ['nazwisko','nrtel',]
    ordering_fields = ['nazwisko',]

class WizytaFilter(FilterSet):
    data_od = DateTimeFilter(field_name='data',lookup_expr='gte')
    data_do = DateTimeFilter(field_name='data',lookup_expr='lte')

    class Meta:
        model = Wizyta
        fields = ['data_od', 'data_do']

class WizytaViewSet(viewsets.ModelViewSet):
    queryset= Wizyta.objects.all()
    serializer_class= WizytaSerializer
    filter_class = WizytaFilter
    search_fields = ['data',]
    ordering_fields = ['data',]
    
class PracownikViewSet(viewsets.ModelViewSet):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer
    filter_fields = ['nazwisko',]
    search_fields = ['nazwisko',]
    ordering_fields = ['nazwisko',]
class PracownikDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pracownik.objects.all()
    serializer_class = PracownikSerializer
    name = 'pracownicy-detail'
class UslugaFilter(FilterSet):
    min_price = NumberFilter(field_name='cena_netto',lookup_expr='gte')
    max_price = NumberFilter(field_name='cena_netto',lookup_expr='lte')
    class Meta:
        model = Usluga
        fields = ['min_price', 'max_price']
class UslugaViewSet(viewsets.ModelViewSet):
    queryset = Usluga.objects.all()
    serializer_class = UslugaSerializer
    filter_class = UslugaFilter
    search_fields = ['nazwa',]
    ordering_fields = ['nazwa','cena_netto',]
class UslugaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Usluga.objects.all()
    serializer_class = UslugaSerializer
    name = 'uslugi-detail'
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'