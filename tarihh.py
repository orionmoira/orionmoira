
from datetime import date

today = date.today()
print("Today: ",today)
# dd/mm/YY
cevrilmisToday = today.strftime("%Y=%d=%m=%Y")
print("Çevrilmiş şekli =", cevrilmisToday, type())
