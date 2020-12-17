from django.db import models
import datetime
# Create your models here.
class Klient(models.Model):
    idKlient = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    nrtel = models.CharField(max_length=100, help_text="schemat:123-456-789")
    class Meta:
        ordering = ('nazwisko',)
    def __str__(self):
        str = "" + self.imie + " " +self.nazwisko + " " + self.nrtel
        return str
class Pracownik(models.Model):
    idPracownik = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=100,help_text="Kilka imion zapisuj po znaku spacji")
    nazwisko = models.CharField(max_length=100, help_text="Nazwiska dwu lub wieloczłonowe pisz po myślniku!")
    class Meta:
        ordering = ('nazwisko',)
    def __str__(self):
        return self.imie + " " + self.nazwisko
class Usluga(models.Model):
    nazwa = models.CharField(max_length=100,primary_key=True)
    cena_netto = models.IntegerField(default=15)
    class Meta:
        ordering = ('nazwa',)
    def __str__(self):
        return self.nazwa + " " + str(self.cena_netto) + "zł"
class Wizyta(models.Model):
    idWizyta = models.AutoField(primary_key=True)
    data = models.DateField()
    godzina = models.TimeField(default=datetime.time)
    pracownicy = models.ManyToManyField(Pracownik)
    uslugi = models.ManyToManyField(Usluga)
    klient = models.ForeignKey(Klient,on_delete=models.CASCADE)
    class Meta:
        ordering = ('data','godzina',)