n = int(input("Sisesta naturaalarv: "))
ruutude_summa = 0
summa_ruut = 0
for i in range (1, n+1):
    ruutude_summa += (i*i)
for i in range (1, n+1):
    if i <= n:
        summa_ruut = i + summa_ruut
        i += 1
print("Summa ruudu ja ruutude summa vahe:",summa_ruut**2 - ruutude_summa)
