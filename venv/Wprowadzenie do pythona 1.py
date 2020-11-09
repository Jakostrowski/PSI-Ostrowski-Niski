# Zadanie 2
tekst = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz' \
        ' w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. ' \
        'przez nieznanego drukarza do wypełnienia tekstem próbnej książki. ' \
        'Pięć wieków później zaczął być używany przemyśle elektronicznym, ' \
        'pozostając praktycznie niezmienionym. Spopularyzował się w ' \
        'latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających' \
        ' fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem' \
        ' Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach' \
        ' osobistych, jak Aldus PageMaker'
imie="Mateusz"
nazwisko="Niski"

liczba_liter1=str(tekst.count(imie[1]))
liczba_liter2=str(tekst.count(nazwisko[1]))

print("W tekscie jest {liczba_liter1} liter {imie[1]} oraz {liczba_liter2} liter {nazwisko[1]}")
# Zadanie 3
# https://pyformat.info/
print('{:^30}'.format('wysrodkowanie'))
print('{: .7f}' . format ( 3.141592653589793 ))
dane  =  { 'imie' :  'Mateusz' ,  'nazwisko' :  'Niski!' }
print('{imie} {nazwisko}' . format ( ** dane ))
print('{:>10}' . format ('tekst'))


# Zadanie 4
zmienna_typu_string = "Może będzie lepiej"
print(dir(zmienna_typu_string))
# help(zmienna_typu_string.split())

# Zadanie 5
L = "Mateusz Niski"
print(L[::-1])

# zadanie 6
lista = list(range(1,11))
srodek=len(lista)//2
pierwsza_polowa=lista[:srodek]
druga_polowa=lista[srodek:]

print(pierwsza_polowa)
print(druga_polowa)

# Zadanie 7
lista = pierwsza_polowa + druga_polowa
lista.insert(0,0)
print(pierwsza_polowa)
print(druga_polowa)
print(lista)

# Zadanie 8
lista_studentow = list()
lista_studentow.append((111111,"Mateusz Niski"))
lista_studentow.append((222222,"Adam Jankowiak"))
lista_studentow.append((333333,"Adrian Merchel"))
lista_studentow.append((444444,"Adrian Plaga"))
lista_studentow.append((555555,"Bartosz Miniszewski"))
lista_studentow.append((666666,"Dominik Saczuk"))
lista_studentow.append((777777,"Piotr Maruszko"))
lista_studentow.append((888888,"Michał Mikowski"))
lista_studentow.append((999999,"Marek Karłowicz"))
lista_studentow.append((101010,"Arkadiusz Nwoacki"))
lista_studentow.append((121212,"Michał Jabłoński"))
lista_studentow.append((131313,"Michał Mikowski"))

# Zadanie 9
dictionary = {}
dictionary['111111'] = ["Mateusz Niski",23,"mateuszniski@poczta.pl","28 luty 1997","Olsztyn"]
dictionary['222222'] = ["Adam Jankowiak",23,"mateuszniski@poczta.pl","28 luty 1997","Olsztyn"]
dictionary['333333'] = ["Adrian Merchel",23,"mateuszniski@poczta.pl","28 luty 1997","Olsztyn"]
dictionary['444444'] = ["Adrian Plaga",23,"mateuszniski@poczta.pl","28 luty 1997","Olsztyn"]
dictionary['555555'] = ["Bartosz Miniszewski",23,"mateuszniski@poczta.pl","28 luty 1997","Olsztyn"]
dictionary['666666'] = ["Dominik Saczuk",23,"mateuszniski@poczta.pl","28 luty 1997","Olsztyn"]

# Zadanie 10
numery = list()
numery = [505022022, 505022022, 501501501,501502502,501501501,532542542]
numery = set(numery)
print(numery)

#zadanie 11
for seq in range(1,11):
    print(seq)
#zadanie 12
for seq in range(100,20,-5):
    print(seq)


# zadanie 13
slownik1 = {}
slownik1 = dict(indeks="jabłko")
slownik2 = {}
slownik2 = dict(indeks="kapusta")
slownik3 = {}
slownik3 = dict(indeks="cukierki")
lista = list()
lista.append(slownik1)
lista.append(slownik2)
lista.append(slownik3)
print("{0} {1} {2}".format(*lista[0].values(),*lista[1].values(),*lista[2].values()))
# Gdy słownik miał więcej niż jedną wartość, to miałem problem  z wypisaniem wszystkich wartości