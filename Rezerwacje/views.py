from django.shortcuts import render
from django.http import HttpResponse,Http404
from rest_framework import viewsets,generics,status
from rest_framework.views import APIView
from .serializers import KlientSerializer,WizytaSerializer,PracownikSerializer,UslugaSerializer
from .models import Klient,Wizyta,Pracownik,Usluga
from rest_framework.response import Response

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

class KlientList(generics.ListCreateAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer
class KlientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Klient.objects.all()
    serializer_class = KlientSerializer

class UslugaList(APIView):
    def get(self,request,format=None):
        uslugi = Usluga.objects.all()
        serializer = UslugaSerializer(uslugi,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer = UslugaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,
            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class UslugaDetail(APIView):
    def get_object(self,pk):
        try:
            return Usluga.objects.get(pk=pk)
        except Usluga.DoesNotExist:
            raise Http404
    def get(self,request,pk,format=None):
        usluga =self.get_object(pk)
        serializer = UslugaSerializer(usluga)
        return Response(serializer.data)
