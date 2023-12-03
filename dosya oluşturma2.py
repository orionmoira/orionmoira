def isimekle():
    print("=== Rehbere Ekleme ===")
    ad      = input ("Adı       :")
    soyad   = input ("Soyadı    :")
    telefon = input ("Telefonu  :")
 
    abc  = open("rehber.txt",  "a")
    eklenecek = ad + "\n"
    abc.write(eklenecek)
    abc.close()


isimekle()
