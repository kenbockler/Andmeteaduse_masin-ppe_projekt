n = int(input('Vali naturaalarv n: '))
r_summa = 0
for i in range(n):
    r_summa += (i + 1)**2
summa = 0
for i in range(n):
    summa += (i + 1)
summa_r = summa**2
vahe = summa_r - r_summa
print(vahe)