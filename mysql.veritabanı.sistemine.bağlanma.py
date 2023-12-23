# veritabanı sistemine bağlanma
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root", password="1234")
print(mydb)
_______
# Bağlanma esnasında hata oluşursa.
import mysql.connector
try:
  mydb = mysql.connector.connect(
    host="localhost", # Community Server yerel bilgisayarda ise localhost olacak.
    user="root", # MySQL WorkBench kurulurken özel bir kullanıcı adı verilmemişse root
    password="1234" # MySQL Community Server kurulumu aşamasında size sorduğu şifre
  )
  print("Bağlantı tamam:", mydb)
except:
  print("Veritabanına bağlanırken bir hata oluştu.")
