def summa(u, v):
    return (u+v)/(1+(u*v)/299792.458**2)
u=float(input('Esimese keha kiirus vaatleja suhtes on: '))
v=float(input('Teise keha kiirus esimese keha suhtes on: '))
x=float(input('Kolmanda keha kiirus teise keha suhtes on: '))
y=float(input('Neljanda keha kiirus kolmanda keha suhtes on: '))
print('Kiiruste summa on:', summa(y, summa(x, summa(u, v))), 'km/s')
    