'''
        n
-----------------
1/a1+ 1/a2...1/an
'''
from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(andmed, n):
    har_kesk= []
    arvud=[]
    indeks=0
    for el in andmed:
        if indeks<(n-1):
            for i in range(indeks+1):
                algne_arv=andmed[i]
                arvud= arvud+[algne_arv]
            har_kesk.append(harmonic_mean(arvud))
            arvud.clear()
            indeks+= 1
        else:
            j= indeks+1-n
            for i in range(j,(j+n)):
                algne_arv=andmed[i]
                arvud= arvud+[algne_arv]
            har_kesk.append(harmonic_mean(arvud))
            arvud.clear()
            indeks+= 1
    return har_kesk
sisend_fail=open(input('Sisesta faili nimi: '))
andmed=[]
for rida in sisend_fail:
    rida= rida.strip('\n').split(',')
    anne= float(rida[1].lstrip())
    andmed.append(anne)
sisend_fail.close()
n= 50
silutud_andmed= silu_andmed(andmed, n)
x_telg= list(range(len(silutud_andmed)))
fig= plt.figure()
ax= fig.add_subplot(1,1,1)
ax.plot(x_telg, andmed)
ax.plot(x_telg, silutud_andmed)
plt.show()