from math import *
n = int(input('Sisestage arv:'))
ruutude_summa = 0
valemi1_arvud = 0
while valemi1_arvud <= n :
    ruutude_summa += int(pow(valemi1_arvud, 2))
    valemi1_arvud += 1
summa_ruut = 0
valemi2_arvud = 0
while valemi2_arvud <= n :
    summa_ruut += valemi2_arvud
    if valemi2_arvud == n :
        summa_ruut **= 2
        break
    valemi2_arvud += 1
summade_vahe = summa_ruut - ruutude_summa
print(str(summade_vahe))