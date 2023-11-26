cbd = []
for a in range(10):
    satir=[]
    for b in range(100):
        satir.append("▓")
        # satir = ▓▓▓▓▓▓▓▓▓
    cbd.append(satir)


print(cbd)
satir1 =""
for xx in cbd:
    for tt in xx:
        # print(tt)
        satir1 += tt
    print(satir1)
    satir1=""
    #print("----------")

    
