c=299792.458
a = float(input("�tle esimese kiirus. "))
b = float(input("�tle teise kiirus. "))
d = float(input("�tle kolmanda kiirus. "))
e = float(input("�tle neljanda kiirus. "))
def summa(u, v):
    kiirus = (u + v)/(1+(u*v)/(c*c))
    return kiirus
kiirusvalgus = summa(summa(summa(a,b),d),e)
print("Kiiruste summa on", kiirusvalgus)