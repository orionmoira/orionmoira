# ad = "Ahmet"
# soyad = "KAYA"
# print (ad,soyad)

class Ogrenci:
        ad = "boş"
        soyad = "boş"
        def __init__(self,x,y):
            self.ad = x
            self.soyad = y


ogrenci1 = Ogrenci
ogrenci2 = Ogrenci
# ogrenci2 = Ogrenci("Musa","AK")
# ogrenci2.ad = "Musa" # init yoksa tüm sınıf
ogrenci2.ad = "Mustafa"
