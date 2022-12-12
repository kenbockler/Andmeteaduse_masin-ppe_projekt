def summa(a,b):
    c= 299792.458
    return (a+b)/(1+((a*b)/c**2))
u = float(input("Palun sisesta esimene kiirus vaatleja suhtes (km/s): "))
v = float(input("Palun sisesta teise keha kiirus esimese keha suhtes (km/s) :"))
x = float(input("Palun sisesta kolmanda keha kiirus teise keha suhtes (km/s):"))
y = float(input("Palun sisesta neljanda keha kiirus kolmanda keha suhtes (km/s):"))
summa1 = summa(u,v)
summa2 = summa(summa1, x)
summa3 = str(summa(summa2, y))
print("Kiiruste summa on " + str(summa3) + " km/s.")