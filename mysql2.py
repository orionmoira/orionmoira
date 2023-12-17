import mysql.connector

try:
  mydb = mysql.connector.connect(
    host="localhost", # Community Server yerel bilgisayara kurulup çalıştırılmışsa localhost olacak.
    user="root", # MySQL Community Server indirip kurunca özel bir kullanıcı adı verilmemişse root olacak
    password="1234" # MySQL Community Server kurulumu aşamasında size sorduğu şifre
  )
  print("Bağlantı tamam:")
  print(mydb)
  print(veritabani)
  try:
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE eticaret")
    print("Veritabanı oluşturuldu.")      
  except:
    print("Veritabanına bağlanırken bir hata oluştu.")

except mysql.connector.Error as hata:
    print(f"Veri tabanı bağlantısı oluşturulamadı. Detay : {hata}")
