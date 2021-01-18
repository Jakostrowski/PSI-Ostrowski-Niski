from rest_framework.test import APITestCase
from . import views
from .models import Klient,Wizyta,Pracownik,Usluga
from rest_framework import status
from rest_framework.reverse import reverse
from django.utils.http import urlencode
from django import urls


class UslugaTests(APITestCase):
    def post_usluga(self, nazwa, cena_netto):
        url = reverse(views.UslugaList.name)
        data = {'nazwa':nazwa,'cena_netto':cena_netto}
        response = self.client.post(url,data,format='json')
        return response
    
    def test_post_and_get_usluga(self):
        nowa_usluga = 'Prostowanie keratynowe'
        nowa_cena = 150
        response = self.post_usluga(nowa_usluga,nowa_cena)
        assert response.status_code == status.HTTP_201_CREATED
        assert Usluga.objects.count() == 1
        assert Usluga.objects.get().nazwa == nowa_usluga
    

    def test_filter_usluga_nazwa(self):
        nowa_usluga = 'Prostowanie zwykłe'
        nowa_cena = 90
        nowa_usluga_1 = 'Farbowanie'
        nowa_cena_1 = 100

        self.post_usluga(nowa_usluga,nowa_cena)
        self.post_usluga(nowa_usluga_1, nowa_cena_1)
        filter_nazwa = {'usluga':nowa_usluga}
        url = '{0}?{1}'.format(reverse(views.UslugaList.name), urlencode(filter_nazwa))
        response = self.client.get(url,format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 2
        assert response.data['results'][1]['nazwa'] == nowa_usluga
    
    def test_post_existing_usluga_name(self):
        url = reverse(views.UslugaList.name)
        nowa_cena = 30
        nowa_usluga = 'Podcinanie końcówek'
        data = {'nazwa':nowa_usluga}
        response_one = self.post_usluga(nowa_usluga,nowa_cena)
        assert response_one.status_code == status.HTTP_201_CREATED
        response_two = self.post_usluga(nowa_usluga,nowa_cena)
        print(response_two)
        assert response_two.status_code == status.HTTP_400_BAD_REQUEST

    def test_get_usluga_collection(self):
        nowa_usluga = 'Fryzura weselna'
        nowa_cena = 100
        self.post_usluga(nowa_usluga,nowa_cena)
        url = reverse(views.UslugaList.name)
        response = self.client.get(url,format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['nazwa'] == nowa_usluga

    def test_update_usluga(self):
        usluga = 'Strzyżenie męskie'
        cena = 30
        response = self.post_usluga(usluga,cena)
        url = urls.reverse(views.UslugaDetail.name,None,[response.data['nazwa']])
        updated_usluga = 'Strzyżenie krótkie'
        updated_cena = 35
        data = {'nazwa': updated_usluga,'cena_netto':updated_cena}
        patch_response = self.client.patch(url,data,format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['nazwa'] == updated_usluga
        assert patch_response.data['cena_netto'] == updated_cena
    
    def test_get_usluga(self):
        usluga = 'Strzyzenie'
        cena = 30
        response = self.post_usluga(usluga,cena)
        url = urls.reverse(views.UslugaDetail.name,None,[response.data['nazwa']])
        get_response = self.client.patch(url,format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['nazwa'] == usluga



class PracownikTests(APITestCase):
    def post_pracownik(self, id, imie, nazwisko):
        url = reverse(views.PracownikList.name)
        data = {'idPracownik':id,'imie':imie,'nazwisko':nazwisko}
        response = self.client.post(url,data,format='json')
        return response

    def test_post_and_get_usluga(self):
        nowy_pracownik_id = 2
        nowy_pracownik_imie = 'Janek'
        nowy_pracownik_nazwisko = 'Kisiel'
        response = self.post_pracownik(nowy_pracownik_id,nowy_pracownik_imie,nowy_pracownik_nazwisko)
        assert response.status_code == status.HTTP_201_CREATED
        assert Pracownik.objects.count() == 1
        assert Pracownik.objects.get().imie == nowy_pracownik_imie
    
    def test_filter_pracownik_nazwa(self):
        nowy_pracownik_id = 2
        nowy_pracownik_imie = 'Janek'
        nowy_pracownik_nazwisko = 'Kisiel'

        nowy_pracownik_id_1 = 3
        nowy_pracownik_imie_1 = 'Konrad'
        nowy_pracownik_nazwisko_1 = 'Gatowski'

        self.post_pracownik(nowy_pracownik_id,nowy_pracownik_imie,nowy_pracownik_nazwisko)
        self.post_pracownik(nowy_pracownik_id_1,nowy_pracownik_imie_1,nowy_pracownik_nazwisko_1)
        filter_nazwisko = {'nazwisko':nowy_pracownik_nazwisko}
        url = '{0}?{1}'.format(reverse(views.PracownikList.name), urlencode(filter_nazwisko))
        response = self.client.get(url,format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 2
        assert response.data['results'][1]['nazwisko'] == nowy_pracownik_nazwisko
    
    def test_get_pracownik_collection(self):
        nowy_pracownik_id = 2
        nowy_pracownik_imie = 'Janek'
        nowy_pracownik_nazwisko = 'Kisiel'
        self.post_pracownik(nowy_pracownik_id,nowy_pracownik_imie,nowy_pracownik_nazwisko)
        url = reverse(views.PracownikList.name)
        response = self.client.get(url,format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['nazwisko'] == nowy_pracownik_nazwisko
    
    def test_update_pracownik(self):
        nowy_pracownik_id = 2
        nowy_pracownik_imie = 'Janek'
        nowy_pracownik_nazwisko = 'Kisiel'
        response = self.post_pracownik(nowy_pracownik_id,nowy_pracownik_imie,nowy_pracownik_nazwisko)
        url = urls.reverse(views.PracownikDetail.name,None,[response.data['idPracownik']])
        updated_pracownik_imie = 'Jaroslaw'
        updated_pracownik_nazwisko = 'Kisielewski'
        data = {'idPracownik':nowy_pracownik_id,'imie':updated_pracownik_imie,'nazwisko':updated_pracownik_nazwisko}
        patch_response = self.client.patch(url,data,format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['nazwisko'] == updated_pracownik_nazwisko
        assert patch_response.data['imie'] == updated_pracownik_imie

    def test_get_usluga(self):
        nowy_pracownik_id = 4
        nowy_pracownik_imie = 'Michał'
        nowy_pracownik_nazwisko = 'Mokak'
        response = self.post_pracownik(nowy_pracownik_id,nowy_pracownik_imie,nowy_pracownik_nazwisko)
        url = urls.reverse(views.PracownikDetail.name,None,[response.data['idPracownik']])
        get_response = self.client.patch(url,format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['idPracownik'] == nowy_pracownik_id

class KlientTests(APITestCase):
    def post_klient(self, id, imie,nazwisko,nrtel,wlasciciel):
        url = reverse(views.KlientList.name)
        data = {'idKlient':id,'imie':imie,'nazwisko':nazwisko,'nrtel':nrtel,'wlasciciel':wlasciciel}
        response = self.client.post(url,data,format='json')
        return response

    def test_post_and_get_klient(self):
        nowy_klient_id = 3
        nowy_klient_imie = 'Antoni'
        nowy_klient_nazwisko = 'Brzęczyszczykiewicz'
        nowy_klient_nrtel = '555-555-555'
        nowy_wlasciciel = 1
        response = self.post_klient(nowy_klient_id,nowy_klient_imie,nowy_klient_nazwisko,nowy_klient_nrtel,nowy_wlasciciel)
        assert response.status_code == status.HTTP_201_CREATED
        assert Klient.objects.count() == 1
        assert Klient.objects.get().nazwisko == nowy_klient_nazwisko
