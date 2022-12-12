pikkus=int(input("Kui pikk peaks elektriliin olema (täismeetrites)? "))
kaugus=int(input("Kui suur on kõrvuti asetsevate postide vahe (täismeetrites)? "))
poste=round(pikkus//kaugus,0)
if pikkus<=kaugus:
    print("Sel juhul on vaja 2 posti!")
elif (pikkus/kaugus-int(poste))==0:
    print("sel juhul on vaja",poste+1,"posti!")
else:
    print("Siis on vaja",poste+2,"posti!")