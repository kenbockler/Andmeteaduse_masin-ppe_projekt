arv = int(input("Sisesta naturaalarv: "))
j = 1
summa = 0
while j <= arv:
    summa += j
    j += 1
summa_ruut = summa ** 2
i = 1
ruutude_summa = 0
while i <= arv:
    ruutude_summa += i ** 2
    i += 1
print(summa_ruut - ruutude_summa)