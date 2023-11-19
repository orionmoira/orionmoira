metin=input("Bir metin girin : ")
 
adet = 0
for harf in metin:
  if harf =="a":
    adet+=1
 
print("Girinlen ifadede {} tane a vardır".format(adet))
