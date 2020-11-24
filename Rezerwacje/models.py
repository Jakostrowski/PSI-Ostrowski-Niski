from django.db import models
import datetime
# Create your models here.

class Klient(models.Model):
    idKlient = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    nrtel = models.CharField(max_length=100)
class Pracownik(models.Model):
    idPracownik = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
class Usluga(models.Model):
    idUsluga = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=100)
    cena_netto = models.IntegerField()
class Specyfikacja(models.Model):
    rabat = models.FloatField()
    cena_sprzedazy = models.IntegerField()
    ilosc = models.IntegerField(default=1)
class Wizyta(models.Model):
    idWizyta = models.AutoField(primary_key=True)
    data = models.DateField(default=datetime.date.today)
    godzina = models.TimeField(default=datetime.time)
    pracownicy = models.ManyToManyField(Pracownik)
    uslugi = models.ManyToManyField(Usluga)
    klient = models.ForeignKey(Klient,on_delete=models.CASCADE)
    spec = models.OneToOneField(Specyfikacja,on_delete=models.CASCADE)