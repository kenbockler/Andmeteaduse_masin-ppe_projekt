number=int(input("Sisesta siia naturaalarv:"))
ruutude_summa = round((number*(number+1)*(2*number+1))/6)
summa_ruut = round((number*(number+1)/2)**2)
print("Summa ruudu ja ruutude summa erinevus on " + str(summa_ruut-ruutude_summa)+".")