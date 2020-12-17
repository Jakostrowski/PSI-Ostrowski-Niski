from rest_framework import serializers
from .models import Klient,Pracownik,Usluga,Wizyta
import datetime
class KlientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = ['idKlient','imie','nazwisko','nrtel']
    def validate_imie(self,value):
        tekst = value.split(' ')
        for i in tekst:
            if i  != i.capitalize():
                raise serializers.ValidationError("Któreś imie z małej litery")
            if not i.isalpha():
                raise serializers.ValidationError("Podano liczby lub inne znaki")
        return value
    def validate_nazwisko(self,value):
        if not value.isalpha() or value!= value.capitalize():
            raise serializers.ValidationError("Nie pasuje")
        return value
    def validate_nrtel(self,value):
        numer = value.replace("-","")
        if not numer.isdigit():
            raise serializers.ValidationError("Nie podawaj liter")
        if len(numer) == 9 and len(value)!=11:
            raise serializers.ValidationError("Nie podano myślników")
        if len(numer)!=9:
            raise serializers.ValidationError("Za krótki lub za długi numer")
        if len(value)==11:
            if value[3]!='-' and value[7]!='-':
                raise serializers.ValidationError("Nie pasuje schemat: 123-456-789")
        return value
    def create(self, validated_data):
        imie = validated_data['imie']
        nazwisko = validated_data['nazwisko']
        nrtel = validated_data['nrtel']
        klient_obj = Klient(
            imie = imie,
            nazwisko= nazwisko,
            nrtel = nrtel
        )
        klient_obj.save()
        return validated_data
class PracownikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pracownik
        fields = '__all__'
    def validate_imie(self,value):
        tekst = value.split(' ')
        for i in tekst:
            if i  != i.capitalize():
                raise serializers.ValidationError("Któreś imie z małej litery")
            if not i.isalpha():
                raise serializers.ValidationError("Podano liczby lub inne znaki")
        return value
    def validate_nazwisko(self,value):
        for char in value:
            if char.isdigit():
                raise serializers.ValidationError("Podano liczby")
        tekst = value.replace(" ","")
        if tekst != value:
            raise serializers.ValidationError("Użyto spacji zamiast myslnika")
        tekst2 = value.split('-')
        for i in tekst2:
            if i != i.capitalize():
                raise serializers.ValidationError("Podano źle nazwisko")
            if not i.isalpha():
                raise serializers.ValidationError("Użyto liczb lub innych znaków")
        return value
class UslugaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usluga
        fields = '__all__'
    #xD nazwa cena_netto
    def validate_cena_netto(self,value):
        if value<15 or value>250:
            raise serializers.ValidationError("Podaj cene z przedzialu <15;250>")
        return value
    def validate_nazwa(self,value):
        tekst = value.split(" ")
        if not value[0].isupper():
            raise serializers.ValidationError("Zacznij z wielkiej litery")
        for i in tekst:
            if not i.isalpha():
                raise serializers.ValidationError("Podano liczby lub inne znaki specjalne")
            if i != i.lower() and i!=tekst[0]:
                raise serializers.ValidationError("Nie uzywaj wielkich znakow poza zaczynającym nazwe")
        return value
    def create(self,validated_data):
        nazwa = validated_data['nazwa']
        cena_netto = validated_data['cena_netto']
        usluga_obj = Usluga(
            nazwa = nazwa,
            cena_netto = cena_netto
        )
        usluga_obj.save()
        return validated_data
class WizytaSerializer(serializers.ModelSerializer):
    klient = serializers.SlugRelatedField(queryset=Klient.objects.all(),slug_field='imie')
    class Meta:
        model = Wizyta
        fields = '__all__'
    #data godzina pracownicy uslugi klient 
    def validate_data(self, value):
        today = datetime.date.today()
        if value < today:
            raise serializers.ValidationError("Wybierz poprawną datę")
        return value
    def validate_godzina(self,value):
        if value.hour<8 or value.hour>15:
            raise serializers.ValidationError("Godziny pracy: 8-16")
        return value
