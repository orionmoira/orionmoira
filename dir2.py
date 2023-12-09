import os
# print(os.listdir())
print("Bulunduğunuz yer:  "+os.getcwd())
for a in os.listdir():
    if os.path.isfile(a):
        print("dosya",end=""+"\t")

        if os.path.isdir(a):
            print("klasör",end=""+"\t")


        print("\t\t",a,end="")
        if a.endswith(".py"):
            print("\t\t(Python dosyası)")
        else: print()
print("\t\t",len(a),"dosya be dizin lsitelendi.")

    
