b = 0
n = int(input("Palun sisestage naturaalarv: "))
for code in range (1, n + 1):
    a = code**2
    b = b + a
i = 1
summa = 0
while i <= n:
    summa += i
    i  += 1
ruutsumma = summa ** 2
finalstep = ruutsumma - b
print(f"Seega esimese {n}. naturaalarvu summa ruudu ja ruutude summa erinevus on {ruutsumma} - {b} = {finalstep}")