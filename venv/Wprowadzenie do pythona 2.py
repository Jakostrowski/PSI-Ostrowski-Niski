# Zadanie 1
def zad_1(a_list,b_list):
    if(len(a_list) > len(b_list)):
        leng = len(a_list)
    else:
        leng = len(b_list)
    lista = [None] * leng
    for i in range(0,len(a_list)):
        if i%2==0:
            lista[i]= a_list[i]
    for j in range(0,len(b_list)):
        if j%2==1:
            lista[j]=b_list[j]
    return lista
lista1 = [2,4,6,8,10]
lista2 = [1,3,5,7]
lista3 = zad_1(lista1,lista2)
print(lista3)
# Zadanie 2
def Slownik(data_text):
    duze =[]
    male =[]
    for i in data_text:
        if i.isupper():
            duze.append(i)
        else:
            male.append(i)
    info = {'length':len(data_text),'letters':list(data_text),'big_letters':duze,'small_letters':male}
    print(info)

txt = "bAduM K"
Slownik(txt)
# Zadanie 3
def Sprawdz(text,letter):
    return text.replace(letter, "")
text='Abecadło Am am'
print(f"{Sprawdz(text,'A')}")
# Zadanie 4
def temperature(celsjusz, temperature_type):
    if isinstance(celsjusz, float) or isinstance(celsjusz, int):
        if temperature_type == 'K':
            print("Kelvin:{0}".format(celsjusz+273.15))
        elif temperature_type == 'F':
            print("Fahrenheit:{0}".format(celsjusz*1.8+32))
        elif temperature_type == 'R':
            print("Rankine:{0}".format((celsjusz + 273.15)*1.8))
        else:
            print("Dane są nieprawidłowe")
    else:
        print("Dane są nieprawidłowe")

temperature(0,'K')
# Zadanie 5
class Calculator:
    def __init__(self, f, s):
        self.a = f
        self.b = s
    def add(self):
        return self.a + self.b
    def difference(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b
kalkulator = Calculator(2,3)
print(f"{kalkulator.add()}")
print(f"{kalkulator.difference()}")
# Zadanie 6
class ScienceCalculator(Calculator):
    def Potegowanie(self):
        return pow(self.a, self.b)
    def Pierwiastek(self):
        return math.sqrt(self.a + self.b)
Kalkulator = ScienceCalculator(2,3)
print(f"{Kalkulator.Potegowanie()}")


# Zadanie 7
def Odwrot(text):
    print(text[::-1])
Odwrot("NO NIE MOGE")
# Zadanie 8
class FileManager:
    def __init__(self, file_name):
        self.file_name=file_name
    def update_file(self, text_data):
        plik=open(self.file_name, 'a' ,encoding='utf-8')
        plik.write(text_data)
    def read_file(self):
        uchwyt = open(self.file_name, 'r', encoding='utf-8')
        while True:
            dane = uchwyt.read(1024)
            print(dane, end='')
            if not dane:
                uchwyt.close()
                break

# Zadanie 9
from Cw2_Zad9 import *
pliczek = FileManager('plik.txt')
pliczek.update_file('KAKAO')
pliczek.read_file()