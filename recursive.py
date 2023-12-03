a = 0
def selamla():
    global a
    a += 1
    print(a)
    print("merhaba")
    print("nasılsın")
    if a == 10 : return a
    else: selamla()


selamla()
