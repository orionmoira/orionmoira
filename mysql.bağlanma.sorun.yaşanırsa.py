import mysql.connector

try:
  mydb = mysql.connector.connect(
    host="localhost", # Server.
    user="root", # Kullanıcı adı.
    password="1234" # Şifre.
  )
  print("Bağlantı tamam:")
  print(mydb)

except:
    print(f"Bağlant hatası. Detay: {mysql.connector.Error}")

