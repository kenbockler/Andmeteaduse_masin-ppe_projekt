def summa(u,v):
    c  = 299792.458
    �lemine = u + v
    alumine = 1 + ((u*v)/(c*c))
    return (�lemine/alumine)
esimene  = float(input("Esimese keha kiirus vaatleja suhtes on: "))
teine = float(input("Teise keha kiirus esimese keha suhtes on: "))
kolmas = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
neljas = float(input("Neljanda keha kiirus kolmanda keha suhtes on:"))
print("Kiiruste summa on ",summa(summa(summa(esimene,teine),kolmas),neljas))