#zad 1 i 2
from datetime import datetime
lorem= "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
imie = "Jakub"
nazwisko = "Ostrowski"
print("W tekscie jest {0} liter k oraz {1} liter r".format(lorem.count(imie[2]),lorem.count(nazwisko[3])))
#zad 3
print("{:>10}".format('test'))
print("{:%Y-%m-%d %H:%M}".format(datetime(1999,2,3,4,5)))
#zad 4
print(dir(lorem))
#help(lorem.encode())
#zad5
print(imie[::-1],nazwisko[::-1])
#zad6
lista = [1,2,3,4,5,6,7,8,9,10]
lista2= lista[5:10]
lista=lista[0:5]
print(lista)
print(lista2)
#zad7
lista=lista+lista2
print(lista)
lista.insert(0,0)
print(lista)
lista2 = lista
print(lista2.sort())
#zad 8
studenci = []
studenci.append((111111,"Raz Raz"))
studenci.append((222222,"Dwa dwa"))
print(studenci)
#zad9
slownik = dict(imie="Jakub")
slownik2 = dict(nazwisko="Ostrowski")
slownik3 = dict(indeks="111111")
slownik4 = dict(wiek=21)
slownik5 = dict(email="test@test.pl")
slownik6 = dict(rok=1999)
slownik7 = dict(adres="Białystok Leśna dolina")
print(slownik)
#zad10
telefony = {"123456789","222222222","333333333","123456789"}
telefony= set(telefony)
print(telefony)
#zad11  12
print(*range(1,11))
print(*range(100,-20,-5))
#zad 13
lista13 = []
lista13.append(slownik)
lista13.append(slownik2)
lista13.append(slownik3)
print("{0} {1} {2}".format(*lista13[0].values(),*lista13[1].values(),*lista13[2].values()))
print("{0} {1} {2}".format(lista13[0],lista13[1],lista13[2]))