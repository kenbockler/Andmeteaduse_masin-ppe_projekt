def summa(u, v):
    c = 299792.458
    summa1 = (u +v)/(1 + ((u*v)/c**2))
    return summa1
u = float(input("Esimese keha kiirus: "))
v = float(input("Teise keha kiirus: "))
x = float(input("Kolmanda keha kiirus: "))
y = float(input("Neljanda keha kiirus: "))
print(summa(summa(summa(u, v), x), y))