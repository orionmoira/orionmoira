def ara():
    # dict, obje, json # yapı olarak aynı
    # import json
    #kayit = {}
    dosya = open("rehber.txt","r")
    okunan = dosya.readline()
    print (okunan)
    print("\nSatır satır")
    for a in dosya:
        #kayıt = json.loads(a)
        print (a)
        #print (type(kayit))
    dosya.close()
