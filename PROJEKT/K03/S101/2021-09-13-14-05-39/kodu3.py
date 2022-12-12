import math
n=int(input("sisesta naturaalarv:"))
m=n
k=0
ruutsum=0
sumruut=int((n*(n+1)/2)**2)
while k<n:
    ruut=m**2
    m-=1
    k+=1
    ruutsum+=int(ruut)
print("naturaalarvu summa ruudu ja ruutude summa erinevus on",(sumruut-ruutsum))
