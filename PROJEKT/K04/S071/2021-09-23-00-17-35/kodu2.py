def summa(u,v):
    vastus = (u + v) / (1 + ((u * v) / 89875517873.68175))
    return(vastus)
keha1 = float(input("Esimese keha kiirus vaatleja suhtes on: "))
keha2 = float(input("Teise keha kiirus esimese keha suhtes on: "))
vastus2 = summa(keha1,keha2)
keha3 = float(input("Kolmanda keha kiirus teise keha suhtes on: "))
vastus1 = summa(vastus2,keha3)
keha4 = float(input("Neljanda keha kiirus kolmanda keha suhtes on: "))
vastus = summa(vastus1,keha4)
print("Kiiruste summa on", vastus,"km/s")