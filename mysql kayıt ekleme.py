import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="orion"
)

mycursor = mydb.cursor()

a= "INSERT INTO ogrenciler (ad, telefon) VALUES (%s, %s)"
b= ("Ensar BUDAK", "05446335847")
mycursor.execute(a, b)

mydb.commit()

print(mycursor.rowcount, " aytır eklendi.")
