def summa(u, v):
    c = 299792.458
    return ( (u+v)/(1 + ((u*v) / ( c**2 ) )))
u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus esimese keha suhtes on: "))
essaJaTeine=summa(u,v)
x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
summaJaKolmas=summa(essaJaTeine,x)
y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
lõplik=summa(summaJaKolmas, y)
print("Kiiruste summa on", lõplik , "km/s")