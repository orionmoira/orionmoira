meyveler = ["Muz","Şeftali","Vişne"]
oyuncular = ["Sacha Boey","Nelsson","İcardi"]

print(meyveler)

# eleman = input("Meyve giriniz:")
eleman = "Kivi"
meyveler.insert(2,eleman)
print("insert ile eklenmiş:",meyveler)
meyveler.insert(2,eleman)
meyveler.pop()
print("pop ile Silinmiş ",meyveler)
meyveler.sort()
print("Sort ile sıralanmış: ",meyveler)
meyveler.reverse()
print("revese ile ters çevirme: ",meyveler)
