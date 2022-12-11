def summa(u, v):
    return (u+v)/(1+((u*v)/(299792.458**2)))
u = float(input('Esimenese keha kiirus vaatleja suhtes on: '))
v = float(input('Teise keha kiirus esimese keha suhtes on: '))
x = float(input('Kolmanda keha kiiruse teise keha suhtes on: '))
y = float(input('Neljanda keha kiiruse kolmanda keha suhtes on: '))
print(summa(summa(summa(u, v), x), y))