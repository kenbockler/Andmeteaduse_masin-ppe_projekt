def summa(u, v):
    return float((u+v)/(1+((u*v)/c**2)))   
u = float(input('Esimese keha kiirus vaatleja suhtes on: '))
v = float(input('Teise keha kiirus esimese keha suhtes on: '))
x = float(input('Kolmanda keha kiirus teise keha suhtes on: '))
y = float(input('Neljanda keha kiirus kolmanda keha suhtes on: '))
c = 299792.458 
summa1 = summa(u, v)
summa2 = summa(summa1, x)
vastus = summa(summa2, y)
print('Kiiruste summa on', vastus, 'km/h.')
