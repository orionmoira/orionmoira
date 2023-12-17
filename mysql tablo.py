# veritabanı dosyasındaki tabloların listesi
import mysql.connector

xxxx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234"
)

aaa = xxxx.cursor()

aaa.execute("CREATE DATABASE orion")

for x in aaa:
    print(x)

