from statistics import harmonic_mean
import matplotlib.pyplot as plt
nimekiri = []
def silu_andmed(järjend,täisarv):
    i = 0
    JärjendiKoopia = järjend[:]
    JärjendiKoopia2 = järjend[:]
    järjend.clear()
    if len(JärjendiKoopia) >= 1:
        while True:
            if i == 0:
                järjend.append(JärjendiKoopia[0])
            elif i != täisarv:
                arvud = JärjendiKoopia2[:i+1]
                järjend.append((harmonic_mean(arvud[0:len(arvud)])))
            if i == täisarv:
                JärjendiKoopia2.pop(0)
                arvud = JärjendiKoopia2[:täisarv]
                järjend.append((harmonic_mean(arvud[0:len(arvud)])))
            JärjendiKoopia.pop(0)
            if i != täisarv:
                i += 1
            if len(JärjendiKoopia) == 0:
                break
    return järjend
failinimi= "aktsiad.txt"
f1=open(failinimi,"r")
sisu = f1.read().replace("\n",",").split(",")
f1.close()
i = 0
while i < len(sisu):
    sisu.pop(i)
    i+=1
uussisu = []
for a in sisu:
    float(a)
    uussisu.append(float(a))
järjend2 = uussisu[:]
arv = 50
xtelg = [list(range(len(järjend2)))]
ytelg = [silu_andmed(uussisu,arv)]
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(xtelg,ytelg)
plt.show()
