n = int(input('Sisesta siia naturaalarv: '))
i = 0
naturaalarvu_ruutude_summa = 0
naturaalarvu_summa = 0
while i < n:
    naturaalarvu_ruutude_summa = naturaalarvu_ruutude_summa + (n * n)
    naturaalarvu_summa = naturaalarvu_summa + (n)
    n = n - 1
naturaalarvu_summa_ruut = naturaalarvu_summa * naturaalarvu_summa
print(naturaalarvu_summa_ruut - naturaalarvu_ruutude_summa)
