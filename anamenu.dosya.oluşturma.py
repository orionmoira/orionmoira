def menu():
    print("╔═════════════════════╗" )
    print("║  REHBER PROGRAMI    ║" )
    print("╠═════════════════════╣" )
    print("║ 1-REHBER EKLE       ║")
    print("║ 2- KAYITLARI LİSTELE║")
    print("║ 3- KAYIT DÜZELT     ║")
    print("║ 4- KAYIT SİL        ║")
    print("║ 5- ÇIKIŞ            ║")
    print("║ SEÇİMİNİZİ GİRİNİZ  ║")
    print("╚═════════════════════╝")
    secim = input()
    if secim == "1":
        rehberEkle()
        listele()
        menu()
    if secim == "2":
        listele()
        menu()
def rehberEkle():
    dosya = open("rehber.txt","a")
    ad=     input("Ad    :  ")
    soyad = input("Soyad  : ")
    numara = input("Numara: ")
    yazilacak = ad +"|"+ soyad +"|"+ numara +"\n"
    dosya.write(yazilacak)
    dosya.close()
def listele():
    try:
        dosya = open("rehber.txt","r")
        print(dosya.readline())
    except:
        print("Dosya bulunamadı.")
        print("Devam etmek için Enter a basın.")
        input()



menu()
