input()
with open("mat.txt")  as  dosya:
  dosya.seek(0) 
  liste = dosya.readlines()
  Fizikten_Kalanlar = []
  Matematikten_Kalanlar = []
  Kimyadan_Kalanlar = []
  for x in range(1,5):
      a = liste[x:x+1]
      Mat_Not = int(a[0][23:26]) 
      Kimya_Not = int(a[0][39:44])
      Fizik_Not = int(a[0][30:35])
      if Mat_Not < 50: 
         Matematikten_Kalanlar.append("{} kişisi Matematikten {} alarak bu dersten kalmıştır.".format(a[0][8:20],a[0][23:26].rstrip()))
      if Kimya_Not < 50: 
         Kimyadan_Kalanlar.append("{} kişisi Kimyadan {} alarak bu dersten kalmıştır.".format(a[0][8:20],a[0][39:44].rstrip()))
      if Fizik_Not < 50: 
         Fizikten_Kalanlar.append("{} kişisi Fizikten {} alarak bu dersten kalmıştır.".format(a[0][8:20],a[0][30:35].rstrip()))
  print("Matematikten kalanlar : ",Matematikten_Kalanlar)
  print("Fizikten kalanlar : ",Fizikten_Kalanlar)
  print("Kimyadan_Kalanlar : ",Kimyadan_Kalanlar)

-close()
