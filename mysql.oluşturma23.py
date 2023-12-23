import mysql.connector

veritababiblgisi = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="orion"
    )

secilenvt = veritababiblgisi.cursor()

sqlkomutu = "SELECT ad,telefon FROM ogrenciler"

secilenvt.execute(sqlkomutu)
alinanlar = secilenvt.fetchall()

#print(alinanlar)
for x in alinanlar:
    print(x)

#for x in alinanlar:
#   print(x[0], "\t",x[1])
