n = int(input("Sisestage naturaalarv: "))
i = 1
summa = 0
while i <= n:
    summa += i**2
    i += 1
o = 1
x = 0
while o <= n:
    x += o
    o += 1
print(x**2 - summa)
    