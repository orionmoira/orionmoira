class Ilan:
    def __init__(self,x,y,z):
        self.ilanno = x
        self.baslik = y
        self.aciklama = z
    def __str__(self)-> str:
        return f"({self.ilanno})"



class Emlak(Ilan):
    def __init__(self,gilanno,gbaslik,gaciklama,gadres,gfiyat):
        self.ilanno = gilanno
        self.baslik = gbaslik 
        self.aciklama = gaciklama
        # super().__init__(gilanno,gbaslik,gaciklama)
        self.adres = gadres
        self.fiyat = gfiyat
    def __str__(self) -> str:
        # super().__str__()
        return f"{self.fiyat}"

emlak1 = Emlak("452","Satılık villa","Sahibin kelepir villa.","Ankara köserlik","300000")
print(emlak1)
print(emlak1.baslik)
