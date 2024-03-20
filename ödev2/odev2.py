import modul
modul.bilgi_ver()
toplam = 0
harfler = "abcdefghijklmnopqrstuvwxyz"
metin = (input("Metin giriniz:"))
harf = (input("harf giriniz:"))
sonuc = modul.buyuk_harf_kucult(metin)
print(sonuc)
if modul.harf_var_mi(metin,harf):
  print("var")
  sonuc1 = modul.kucuk_harf_buyult(metin)
  print(sonuc1)
else:
  print("yok")

harf_sayisi = modul.harf_adeti(metin)

for harf,sayi in harf_sayisi.items():
    if (harf in harfler):
        toplam += sayi

for harf,sayi in harf_sayisi.items():
    if (harf in harfler):
        print(f"'{harf}' : {sayi} adet  => %{((100*sayi)/toplam):.2f}")

       
  