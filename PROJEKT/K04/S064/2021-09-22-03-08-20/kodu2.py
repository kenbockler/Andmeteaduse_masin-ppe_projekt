def summa(u, v):
    c = 299792.458
    summa = (u + v)/(1 + (u*v/c**2))
    return summa
u = float(input("Esimese keha kiirus vaatleja suhtes on: "))
v = float(input("Teise keha kiirus esimese keha suhtes on: "))
x = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
y = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
teine = summa(u, v)
kolmas = summa(teine, x)
neljas = summa(kolmas, y)
print("Kiiruste summa on", neljas, "km/s.")