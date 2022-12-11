n = int(input("Sisestage n: "))
a = 0
b = 0
rs = 0
s = 0
sr = 0
while a < n:
    a += 1
    rs = rs + (a**2)
while b < n:
    b += 1
    s += b
else:
    sr = (s**2)
vahe = sr - rs
print("Summa ruudu ja ruutude summa vahe on " + str(vahe) + ".")