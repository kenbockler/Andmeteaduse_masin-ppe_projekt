def summa (u,v):
    c=299792.458
    avaldis=(u+v)/(1+((u*v)/c**2))
    return avaldis
a=float(input('Esimese keha kiirus vaatleja suhtes on: '))
b=float(input('Teise keha kiirus esimese keha suhtes on: '))
c=float(input('Kolmanda keha kiirus teise keha suhtes on: '))
d=float(input('Neljanda keha kiirus kolmanda keha suhtes on: '))
kiirus=summa(summa(summa(a,b), c), d)
print('Kiiruste summa on '+str(kiirus)+' km/s')