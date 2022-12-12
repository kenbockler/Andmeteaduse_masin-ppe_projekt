n = i = int(input("Sisesta naturaalarv: "))
summa = 0
b=0
p=0
while b <= n:
    summa += b**2
    b += 1
print(summa)
summa2=0
while p <= i:
    summa2 += p
    p += 1
print(summa2)
erinevus=summa2**2-summa
print(erinevus)
