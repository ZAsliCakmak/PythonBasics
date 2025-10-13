from abc import ABC, abstractmethod
from math import *  # tüm math library getirir
import math as matematik
import random
import time
import numpy as np


# Print fonksiyonu ve built in function
print("Zeynep Aslı")
print("Zeynep", "Aslı", "Çakmak", sep='.')

# Veri tipleri
x = 5  # integer
y = "Asli"  # string
z = 'k'  # char
t = 3.5  # float

# Veri Yapıları

# Birden farklı veri tipini tutan diziler
liste1 = [1, 3, 3, 5, 4, 5, 4, "ali", "canan"]
liste1[0]  # 1 sayısı
a = len(liste1)
b = dir(liste1)  # built in functions
print(a)

liste2 = [1, 3, 3, 5, 4, 5, 4]
liste2.sort(reverse=True)  # Azalan sırada listeyi sıralamak için
print(liste2)
liste2[0] = 250
print(liste2[0])
print(liste2)

liste2.pop(0)  # Artık listenin ilk elemanı olan 250 listeden çıkarıldı
liste2.append(25)  # Listenin sonuna yeni eleman ekleme
liste2.insert(7, "25")  # Listenin istenilen indexine eleman ekleme
print(liste2)
# Artık listedeki 7. indexte-burada sonu oluyor- 25 elemanı eklendi
print(liste2[7])

demet = ("ali", "ayşe")
demet
len(demet)  # Bu fonksiyon demet listesindeki eleman sayısını veriyor-length-
demet[0]  # ali elemanı
dir(demet)
print(demet.count("ali"))  # Ali nin listede kaçıncı sırada olduğu
print(demet.index("ali"))  # 'ali' elemanı index ve sıra farklı

c = "zeynep"
type(c)  # veri tipi gösteren fonksiyon -string-
c.capitalize()  # Değişken stringse baş harfini büyük yapar.


def toplam(deger, deger2):
    x = deger+deger2
    print("{}, {} değerlerini alır ve sonuç {} 'tir ".format(deger, deger2, x))


def topla(parametre):
    # iki tane fonksiyon tanımlansa da pyhtonda en son tanımlanan fonksiyon kabul edilir -override-
    print("alınan degerleri: ", parametre)
# Bu yüzden fonksiyonlardan bir tanesinin ismini topla -> toplam yapıyorum


topla(5)
toplam(3, 5)


def selam():
    print("selam")


selam()  # parametre almayan, değer döndürmeyen fonksiyon


def selamGotur(isim):
    print("selam", isim)


selamGotur("Asli")  # parametre alan , değer döndürmeyen fonksiyon


def cikarma(a, b):
    y = a-b
    print("Sonuç : {}".format(y))


cikarma(8, 2)  # parametre alan , değer döndüren fonksiyon

# help(print) ---> built in function(yerleşik fonksiyon yani zaten pyhton ın içinde olan fonksiyonlar)


def toplama(a, b):  # değer döndüren ve parametre alan fonksiyon yine
    c = a+b
    return c


k = toplama(4, 9)
print(k)


def kareal(a):
    return a*a


sonuc = kareal(3)
print("istenilen değerin karesi : {} ".format(sonuc))

# Kullanıcıdan veri girişi
a = int(input("1. sayıyı giriniz: "))
b = int(input("2. sayıyı giriniz: "))


def cikar(x, y):
    print("sonuc :", a-b)
    return a-b


cikar(x, y)


def kareal(x):
    # print("a nın karesi:",a*a)
    return a*a


sonuc = cikar(a, b)
kareal(a)
cikar(5, 5)


def ceyrek(x):
    return x/4


def küpal(x):
    return x*x*x


küp = küpal(3)
print(küp)

bölüm = ceyrek(4)
print(bölüm)

küpal(ceyrek(12))
print(küpal(ceyrek(20)))

liste1 = [1, 2, 3, 4, 5]
liste1  # tek boyutlu dizi
# Liste1 deki elemanları ikiyle çarpıp liste2 ye oluşturdu
liste2 = [i*2 for i in liste1]
print(liste2)


def kare(x): return x*x  # kare al fonksiyonu yerine


def toplama(x, y):
    return x+y


toplama(5, 5)

# lambda=  return kullanmadan tek satırlı fonksiyon ifade biçimi (argümanlar : ifade)


def toplama(x, y): return x+y


print(toplama(5, 5))


print(matematik.pow(2, 2))
print(2**2)
print(matematik.cos(60))
print(matematik.sin(60))

print(matematik.sqrt(4))


# verilen aralıkta rastgele bir değer yazdırır.
rastgele = random.randint(1, 100)
print(rastgele)


rastgele = random.randint(1, 100)
tahmin = 5

# Buradaki fonksiyon tahmin edilen sayı rastgele değişkeniyle aynı çıkana kadar direktif veriyor.
while True:
    tahmin = int(input("tahmin gir 1-100 arası :"))
    print("kontrol ediliyor")
    if (tahmin == rastgele):
        print("kontrol ediliyor")
        time.sleep(1)
        print("girilen sayi", tahmin)
        print("tebrikler")
        break
    elif (tahmin < rastgele):
        tahmin = tahmin-1
        print("sayıyı büyült")
    elif (tahmin > rastgele):
        tahmin = tahmin-1
        print("sayıyı küçült")
    else:
        print("1-100 de değer gir")
    if (tahmin == 0):
        print("hak bitti")
        break


a = 5
string = "dogus"
isci_ismi = "ali"
isci_yas = 50
isci_adres = "Üsküdar"
# ---> NESNE TABANLI PROGRAMLAMADA BİR NESNE İÇİN AYRI AYRI DEĞİŞKENLER OLUŞTURMAK YERİNE BİR NESNE OLUŞTURUP FARKLI ÖZELLİKLER ATARIZ.
isci_kurum = "dogus"
# Bu özellikleri bir arada tutan yapıya ise class denir.


class Calisan():
    def __init__(self, ad, soyad, maas, departman):
        self.isim = ad
        self.soyisim = soyad
        self.maas = maas
        self.departman = departman


calisan1 = Calisan("Zeynep Asli", "Çakmak", 55000, "I.T.")


class Arac():
    def __init__(arac, color, modell, brand):
        arac.renk = color
        arac.model = modell
        arac.marka = brand


# Nesne oluşturduk ve nesnenin özelliklerini belirttik
a1 = Arac("Sari", "Jeep", "Kia")


print(a1)  # a1 bir objedir çıktısı veriyor.
print(a1.marka)
print(a1.model)
print(a1.renk)
a1.marka = "BMW"
print(a1.marka)


class Kare():
    def __init__(şekil, edge):
        şekil.kenar = edge

    def alan(self):
        alan = self.kenar*self.kenar
        return alan


k1 = Kare(4)

print(k1.kenar)
print(k1.alan())


class Isci():
    yas = 20    # Sınıf Değişkeni (Tüm Isci nesneleri için varsayılan)
    maas = 1000  # Sınıf Değişkeni

    def yasaGoreMaasOranla(self):
        # self.yas ve self.maas ile nesnenin özelliklerine erişir.
        print(self.yas / self.maas)


isci1 = Isci()            # Isci sınıfından bir nesne (isci1) türetildi.
isci1.yasaGoreMaasOranla()  # isci1 nesnesinin metodu çağrıldı.


def yasMaasOranı(yas, maas):  # class dışı metot
    # Parametre olarak aldığı değerlerle işlem yapar.
    a = yas / maas
    # print("oran:\t", a) # Bu satır yoruma alınmış.
    print("oran:\t {}".format(a))


yasMaasOranı(20, 2000)  # Fonksiyon doğrudan çağrıldı.


class Hayvan():
    def __init__(self, isim, yas):  # yapıcı/constructor metot
        self.isim = isim
        self.yas = yas

    def getYas(self):
        return self.yas

    def getAd(self):
        return self.isim


h1 = Hayvan("dog", 2)
h1_yas = h1.getYas()
print("h1 in yaşı :", h1_yas)

h1_isim = h1.getAd()
print("h1 in isim :", h1_isim)

h2 = Hayvan("cat", 3)
h2_yas = h2.getYas()
print("h2 in yaşı :", h2_yas)


class Makine():
    def __init__(self, a, b):
        self.deger1 = a
        self.deger2 = b

    def topla(self):
        sonuc = self.deger1+self.deger2
        return sonuc

    def carp(self):
        sonuc = self.deger1*self.deger2
        return sonuc

    def cikar(self):
        return self.deger1-self.deger2

    def bol(self):
        return self.deger1/self.deger2


# Kullanıcıdan klavye ile dışarıdan değer alma
x = float(input("Birinci sayıyı girin: "))
y = float(input("İkinci sayıyı girin: "))

h: Makine = Makine(x, y)
tSonuc = h.topla()
cSonuc = h.carp()
print("toplama sonuc: {}, çarpma sonucu: {}".format(tSonuc, cSonuc))

# Burada değişkenler public olduğunda dışarıdan kolayca erişilebiliyor; bu yüzden private yapıp get,set metotlarıyla almamız gerekiyor


class Banka():
    def __init__(self, isim, para, adres):
        self.isim = isim
        self.para = para
        self.adres = adres


hesap1 = Banka("Sinan", 1000, "istanbul")
hesap2 = Banka("Ayşe", 5000, "Erzurum")
print(hesap1.para)
hesap2.para = hesap2.para+hesap1.para  # sinan'ın parası kalmadı
print(hesap2.para)
hesap1.para = 0
print(hesap1.para)


class Banka2():
    def __init__(self, isim, para, adres):
        self.__isim = isim
        self.__para = para
        self.__adres = adres
# get ve set metotları

    def getPara(self):
        return self.__para

    def setPara(self, miktar):
        self.__para = miktar

    def islemSayisi(self):
        self.__para = self.__para-10


hes1 = Banka2("Sinan", 1000, "istanbul")
hes2 = Banka2("Ayşe", 5000, "Erzurum")
print("1. hesaptaki para: ", hes1.getPara())
hes1.setPara(100)
print("set işlemi sonrası 1. hesaptaki para değişimi :", hes1.getPara())
hes1.islemSayisi()
print("işlem ücreti :", hes1.getPara())


"""class Animal():
    def __init__(self):
        print("hayvan sınıfının yapıcı metotum")

    def sesCikar(self):
        print("hav,miyav,vak....")

    def hareket(self):
        print("zıplar,koşar,yürür..")
# cocuk sınıf ----child


class kedi(Animal):
    def __init__(self):
        super().__init__()  # yazmasakta olur ata sınıfın init metodunu ezeriz metot overriding!!
        print("kedi sınıfı oluşturuldu")

    def sesCikar(self):
        print("miyav")

    def DokuzCan(self):  # diğer hayvanlardan ayrılan bir fonksiyon :D
        print("Bu sevimli hayvanlar hep dört ayak üstüne düşer")


k1 = kedi()
k1.sesCikar()  # ata sınıfı ezer, kedi classındaki sesCıkar çağrılır.
k1.hareket()  # ata sınıfından miras
k1.DokuzCan()


class kus(Animal):
    def __init__(self):
        print("kus sınıfı oluşturldu")

    def ucma(self):
        print("kanatları vardır uçarlar")


kus1 = kus()
kus1.ucma()
kus1.hareket()  # ata sınıftan miras"""


class Animal(ABC):  # super clas
    @abstractmethod
    def yurume(self): pass
    @abstractmethod
    def kosma(self): pass  # sablon oluşturup tekrar tekrar kullan


class kus(Animal):
    def __init__(self):
        print("kuş oluşturuldu")

    def yurume(self):
        print("kuslar pek yürümez")

    def kosma(self):
        print("kuslar pek kosmazda")


# a=Animal() soyut sınıflardan nesne oluşturulmaz.
b = kus()  # abstract clasın içeriği yavru sınıfta doldurulur.
b.kosma()
b.yurume()


class Animal():
    def sesVer(self):
        print("ses çıkarırlar")


class kedi(Animal):
    def sesVer(self):  # ata sınıfı ezdi
        print("miyav")


a = Animal()
a.sesVer()
k = kedi()
k.sesVer()  # Overload: aynı isme sahip bir metot veya operatörün,
# farklı sayıda veya farklı tipte parametreler alarak farklı işlevler gerçekleştirmesi yeteneğidir.


class Hayvanlar:
    def __init__(self, isim):
        self.isim = isim

    def tepki(self):
        raise NotImplementedError('HATA')


class Kedi(Hayvanlar):
    def tepki(self):
        return 'Miyav!'


class Kopek(Hayvanlar):
    def tepki(self):
        return 'Haav! Hav!'


hayvan = [Kedi('Boncuk'), Kedi('Tekir'), Kopek('Elmas')]
for hyvn in hayvan:
    # Aynı isimde fakat farklı içerikteki fonksiyonları nesneler farklı olduğu için hepsinin çıktısı
    print(hyvn.isim + ': ' + hyvn.tepki())
    # farklı olacak şekilde kullanabiliyoruz.


class Animal():
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def talk(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Cat(Animal):
    def talk(self):
        return 'Meow!'


class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'


animals = [Cat('Missy'), Cat('Mr. Mistoffelees'), Dog('Lassie')]
for animal in animals:
    print(animal.name + ': ' + animal.talk())

    """Polimorfizm sayesinde, farklı nesne türleri üzerinde tek bir arayüz (interface) 
 (animal.talk()) kullanarak, o nesneye özgü davranışları (miyavlama, havlama) gerçekleştirebiliriz."""
