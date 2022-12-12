def summa(u, v):
    a = u + v
    b = 1 + u * v / 299792.458 ** 2
    c = a / b
    return c
def num(t):
    i = ""
    while(True):
        try:
            t = float(t)
            if t > 299792.458:
                i = float(i)
            else:
                return t
        except:
            t = input("Sisestage kiirus numbriga[peab olema väiksem kui valguskiirus(km/s)]: ")
a = input("Esimese keha kiirus: ")
a = num(a)
b = input("Teise keha kiirus esimese keha suhtes: ")
b = num(b)
x = input("Kolmanda keha kiirus teise keha suhtes: ")
x = num(x)
y = input("Neljanda keha kiirus kolmanda keha suhtes: ")
y = num(y)
sum1 = summa(a, b)
sum2 = summa(sum1, x)
sum3 = summa(sum2, y)
print("Kiiruste summa on", sum3,"km/s.")