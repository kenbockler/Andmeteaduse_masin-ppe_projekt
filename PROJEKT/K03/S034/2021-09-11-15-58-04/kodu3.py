n = int(input("Palun sisesta naturaalarv n: "))
if n < 0:
    print("Sisestatud arv pole naturaalarv. Proovi arve 0, 1, 2, 3, ... jne.")
elif n >= 0:
    summa_ruut = int((n*(n+1)/2)**2)
    ruutude_summa = 0
    for n in range (1, n+1):
        ruutude_summa = ruutude_summa + (n*n)
    lahend = str(summa_ruut - ruutude_summa)
    print("Esimese " + str(n) + " naturaalarvu summa ruudu ja ruutude summa erinevus on " + lahend + "." )