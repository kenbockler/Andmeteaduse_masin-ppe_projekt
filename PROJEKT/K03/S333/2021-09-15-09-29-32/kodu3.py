n = int(input("Sisesta naturaalarv: "))
i= 1
ruudud= 0
summa= 0
while i <= n:
    lüli_1= (1*i)**2
    ruudud += lüli_1
    i +=1
print('Ruutude summa on: '+ str(ruudud))
i-=n
while i <= n:
    lüli_2= (1*i)
    summa += lüli_2
    i +=1
summa_ruut= summa**2
print('Summa ruut on: '+ str(summa_ruut))
erinevus= summa_ruut- ruudud
print('Esimese',n , 'naturaalarvu summa ruudu ja ruudude summa erinevus on:', erinevus)
