def summa(u,v):
    c=299792.458
    summa=(u+v)/(1+(u*v/c**2))
    return summa
u=float(input("Esimese keha kiirus vaatleja suhtes on: "))
v=float(input("Teise keha kiirus vaatleja suhtes on: "))
x=float(input("Kolmanda keha kiirus vaatleja suhtes on: "))
y=float(input("Neljanda keha kiirus vaatleja suhtes on: "))
summa2=summa(summa(u,v),summa(x,y))
print("Kiiruste summa on "+str(summa2)+" km/s.")