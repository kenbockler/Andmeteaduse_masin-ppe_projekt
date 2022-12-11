from statistics import harmonic_mean
import matplotlib.pyplot as plt
nimi=str(input("Sisesta faili nimi: "))
arv=int(input("Sisesta täisarv, mis näitab mitme elemendi kaupa keskmistamist rakendatakse: "))
f=open("nimi", "r")
def silu_andmed(xoxox,arv):
    jarjend=[]
    for indeks in range(1,len(xoxox)+1):
        algus= max(0, indeks-arv)
        j=harmonic_mean(xoxox[algus:indeks])
        jarjend.append(j)
    return jarjend
funktsiooni=[]
for i in f:
    strip = i.strip()
    split = strip.split()
    viimane=split.pop()
    funktsiooni.append(viimane)
funktsiooni = list(map(float, funktsiooni))
peeter=(silu_andmed(funktsiooni,arv))
plt.plot(funktsiooni)
plt.plot(peeter)
plt.show()
