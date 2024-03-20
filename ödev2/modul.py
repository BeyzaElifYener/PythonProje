def harf_adeti(metin):
    harf_sayisi = {}
    for harf in metin:
        harf = harf.lower()
        if harf in harf_sayisi:
            harf_sayisi[harf]+=1
        else:
            harf_sayisi[harf]=1
    return harf_sayisi

def buyuk_harf_kucult(metin):
   
    return metin.lower()

def harf_var_mi(metin, harf):
    
    return harf in metin

def kucuk_harf_buyult(metin):

    return metin.upper()

def bilgi_ver():
  
    print("Ad: Beyza Elif")
    print("Soyad: Yener")
    print("Öğrenci Numarasi: 211220009")
    print("Not: Selam Dünya")


    