# Kullanıcıdan Alınan Metni Ekranda Gösterme
import math
import random
kelime = input("Anahtar kelimeyi giriniz: ")
print(kelime)
# Kullanıcının Girdiği İki Sayıyı Toplama
number1 = int(input("1. sayıyı girin: "))
number2 = int(input("2. sayıyı girin: "))
toplam = number1 + number2
print("Toplam:", toplam)
# Girilen Sayının Tek veya Çift Sayı Olduğunu Belirleme
sayi = int(input("Bir sayı girin: "))
if sayi % 2 == 0:
    print("Girdiğiniz sayı çifttir.")
else:
    print("Girdiğiniz sayı tektir.")
# İki Sayı ile İşlem Yapan Basit Hesap Makinesi
sayi1 = float(input("1. sayıyı girin: "))
sayi2 = float(input("2. sayıyı girin: "))
islem = input("İşlem seçin (+, -, *, /): ")

if islem == "+":
    print("Sonuç:", sayi1 + sayi2)
elif islem == "-":
    print("Sonuç:", sayi1 - sayi2)
elif islem == "*":
    print("Sonuç:", sayi1 * sayi2)
elif islem == "/":
    if sayi2 != 0:
        print("Sonuç:", sayi1 / sayi2)
    else:
        print("Sıfıra bölme hatası!")
else:
    print("Geçersiz işlem!")
# Hesap Makinesinde Kullanıcı Hatalarını Önleme
try:
    sayi1 = float(input("1. sayıyı girin: "))
    sayi2 = float(input("2. sayıyı girin: "))
    islem = input("İşlem seçin (+, -, *, /): ")

    if islem == "+":
        print("Sonuç:", sayi1 + sayi2)
    elif islem == "-":
        print("Sonuç:", sayi1 - sayi2)
    elif islem == "*":
        print("Sonuç:", sayi1 * sayi2)
    elif islem == "/":
        print("Sonuç:", sayi1 / sayi2)
    else:
        print("Geçersiz işlem!")
except ValueError:
    print("Lütfen geçerli bir sayı girin!")
except ZeroDivisionError:
    print("Sıfıra bölme hatası!")
# +/- İşaretine Her Basıldığında Sayıyı Arttırma/Azaltma
sayi = 0
while True:
    secim = input("+ için artır, - için azalt, q için çık: ")
    if secim == "+":
        sayi += 1
        print("Sayı:", sayi)
    elif secim == "-":
        sayi -= 1
        print("Sayı:", sayi)
    elif secim == "q":
        break
# +10 ile -10 Arasındaki Sayıları Ekrana Yazma
for i in range(-10, 11):
    print(i)
# Metindeki Her Harfin Arasına Virgül Koyma
metin = input("Bir metin girin: ")
sonuc = ",".join(metin)
print(sonuc)
# 1 ile 100 Arasında Rastgele 10 Tam Sayı Üretip Dizi İçine Ekleme

dizi = []
for i in range(10):
    dizi.append(random.randint(1, 100))
print(dizi)
# -100 ile +100 Arasındaki 5’e Tam Bölünen Sayıları Yan Yana Gösterme
for i in range(-100, 101):
    if i % 5 == 0:
        print(i, end=" ")
# Üç Adet Sayıyı Karşılaştırıp Sıralama
sayi1 = int(input("1. sayı: "))
sayi2 = int(input("2. sayı: "))
sayi3 = int(input("3. sayı: "))

liste = [sayi1, sayi2, sayi3]
liste.sort()
print("Sıralı hali:", liste)
# Faktöriyel Hesaplama ve Açılımını Yazdırma
sayi = int(input("Bir sayı girin: "))
faktoriyel = 1
acilim = ""

for i in range(sayi, 0, -1):
    faktoriyel *= i
    acilim += str(i)
    if i > 1:
        acilim += "."

print(acilim, "=", faktoriyel)
# Metindeki İlk Kelime ile Son Kelimeyi Bulma
metin = input("Bir metin girin: ")
kelimeler = metin.split()
print("İlk kelime:", kelimeler[0])
print("Son kelime:", kelimeler[-1])
# Girilen Sayıların Toplamını ve Ortalamasını Bulma
sayilar = input("Sayıları boşlukla ayırarak girin: ")
liste = [int(x) for x in sayilar.split()]
toplam = sum(liste)
ortalama = toplam / len(liste)
print("Toplam:", toplam)
print("Ortalama:", ortalama)
# Büyük Harfleri Küçük Harflere, Küçük Harfleri Büyük Harflere Dönüştürme
metin = input("Bir metin girin: ")
sonuc = metin.swapcase()
print(sonuc)
# Personel Maaşından Yüzdesel Zam Hesaplama
maas = float(input("Maaşı girin: "))
zam_orani = float(input("Zam oranını girin (%): "))
zam_miktari = maas * zam_orani / 100
yeni_maas = maas + zam_miktari
print("Zam miktarı:", zam_miktari)
print("Yeni maaş:", yeni_maas)
# Sayı Değerlerinin Toplamını Hesaplama
sayi = input("Bir sayı girin: ")
toplam = sum(int(rakam) for rakam in sayi)
print("Rakamların toplamı:", toplam)
# Kullanıcının Sonsuz Sayıda Girdiği Değerlerin Yanına Tek/Çift Yazma
while True:
    sayi = input("Bir sayı girin (çıkmak için 'q'): ")
    if sayi == 'q':
        break
    sayi = int(sayi)
    if sayi % 2 == 0:
        print(sayi, "- Çift")
    else:
        print(sayi, "- Tek")
# 1 ile 300 Arasındaki Sayılardan 11 Sayısına Bölünenleri Bulma
for i in range(1, 301):
    if i % 11 == 0:
        print(i, end=" ")
# Mutlak Sistemde Sınıfı Geçmek İçin Gereken Final Notunu Hesaplama
vize = float(input("Vize notunu girin: "))
vize_yuzdesi = float(input("Vize yüzdesini girin (%): "))
final_yuzdesi = 100 - vize_yuzdesi
gecme_notu = 60

gereken_final = (gecme_notu - (vize * vize_yuzdesi / 100)) / \
    (final_yuzdesi / 100)
print("Geçmek için gereken final notu:", gereken_final)
# Üç Kenarı Girilen Üçgenin Alanını Hesaplama

a = float(input("1. kenar: "))
b = float(input("2. kenar: "))
c = float(input("3. kenar: "))

u = (a + b + c) / 2
alan = math.sqrt(u * (u - a) * (u - b) * (u - c))
print("Üçgenin alanı:", alan)
# Metindeki Sesli Harf Sayısını Hesaplama
metin = input("Bir metin girin: ").lower()
sesliler = "aeıioöuü"
sayac = 0

for harf in metin:
    if harf in sesliler:
        sayac += 1

print("Sesli harf sayısı:", sayac)
# Her Sayıyı Kendisi Kadar Yan Yana Yazdırma
sayi = input("Bir sayı girin: ")
print(sayi * int(sayi))
# Tekrarsız Rastgele Sayı Üretme

dizi = random.sample(range(1, 101), 10)
print(dizi)
# Asal Çarpanlarını Bulma
sayi = int(input("Bir sayı girin: "))
carpanlar = []
bolen = 2

while sayi > 1:
    if sayi % bolen == 0:
        carpanlar.append(bolen)
        while sayi % bolen == 0:
            sayi = sayi // bolen
    bolen += 1

print("Asal çarpanlar:", carpanlar)
# Metindeki En Uzun Kelimeyi Bulma
metin = input("Bir metin girin: ")
kelimeler = metin.split()
en_uzun = max(kelimeler, key=len)
print("En uzun kelime:", en_uzun)
# Girilen Bir Notun Harf Karşılığını Bulma
not_degeri = float(input("Notu girin: "))

if not_degeri >= 90:
    print("AA")
elif not_degeri >= 85:
    print("BA")
elif not_degeri >= 80:
    print("BB")
elif not_degeri >= 75:
    print("CB")
elif not_degeri >= 70:
    print("CC")
elif not_degeri >= 65:
    print("DC")
elif not_degeri >= 60:
    print("DD")
elif not_degeri >= 50:
    print("FD")
else:
    print("FF")
# Cümledeki Her Kelimeyi Tersten Yazdırma
cumle = input("Bir cümle girin: ")
kelimeler = cumle.split()
ters_kelimeler = [kelime[::-1] for kelime in kelimeler]
print(" ".join(ters_kelimeler))
# Metni Mors Alfabesine Çevirme
mors = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': '/'
}

metin = input("Bir metin girin: ").upper()
mors_metin = ' '.join(mors.get(harf, '') for harf in metin)
print(mors_metin)
# Kümülatif Toplam Hesaplama
sayilar = [1, 2, 3, 4, 5]
kumulatif = []
toplam = 0

for sayi in sayilar:
    toplam += sayi
    kumulatif.append(toplam)

print("Orijinal:", sayilar)
print("Kümülatif:", kumulatif)
