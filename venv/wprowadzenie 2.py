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

def zad_2(data_text):
    a1 = []
    a2 = []
    for i in data_text:
        if i.isupper():
            a1.append(i)
        else:
            a2.append(i)
    dict = {'length': len(data_text), 'letters': list(data_text), 'big_letters': a1, 'small_letters': a2}
    return dict

text="YmCa"
print(zad_2(text))

def zad_3(text,letter):
    return text.replace(letter,"")
t1 = "hahaha"
print(zad_3(t1,'a'))

def zad_4(c,type):
    if (type == 'F' or type=='f'):
        print("Fahrenheity: {0}".format(c*1.8+32))
    elif (type == 'K' or type=='k'):
        print("Kelviny: {0}".format(c+273.15))
    elif (type == 'R' or type=='r'):
        print("Rankiny: {0}".format((c+273.15)*1.8))

zad_4(5,'r')

class Kalkulator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def difference(self):
        return self.x - self.y
    def multiply(self):
        return self.x * self.y
    def divide(self):
        return self.x / self.y

kalkulator = Kalkulator(3,4)
print(kalkulator.add())
print(kalkulator.multiply())


class ScienceCalculator(Kalkulator):
    def Potegowanie(self):
        return pow(self.x, self.y)

kalkulator_specjalny = ScienceCalculator(3,4)
print(kalkulator_specjalny.Potegowanie())

def zad_7(tekst):
    return tekst[::-1]

print(zad_7("haha"))

from wprowadzenie_2_filemanager import *


plik= FileManager('plik.txt')
plik.update_file("lololo")
plik.read_file()