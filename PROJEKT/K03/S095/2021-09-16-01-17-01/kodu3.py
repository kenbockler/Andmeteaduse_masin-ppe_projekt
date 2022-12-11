naturaalarv=int()
while naturaalarv<=0:
    naturaalarv=int(input("Sisesta Naturaalarv: "))
summa=0
summaruut=0
ruutudesumma=0
while summa<naturaalarv:
    summa=summa+1
    summaruut+=summa
    ruutudesumma+=summa**2
summaruut=summaruut**2
erinevus=summaruut-ruutudesumma
print("Summaruudu ja ruutude summa erinevus on: ", erinevus)
    