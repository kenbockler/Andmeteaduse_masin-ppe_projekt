from statistics import harmonic_mean
from matplotlib.pyplot import *
n = input("Sisestage täisarv: ")
f = open("aktsiad.txt")
aktsiad = []
for rida in f:
    a = rida.strip().split()
    aktsiad.append(float(a[-1]))
def silu_andmed(aktsiad, n):
    suvaline = []
    keskmistatud = []
    for x in range (0, len(aktsiad)):
        suvaline.append(aktsiad[x])
        if len(suvaline) >= int(n):
            suvaline.pop(0)
        keskmistatud.append(harmonic_mean(suvaline))
    return(keskmistatud)
päevad = list(range(0, len(aktsiad)))
fig = figure()
ax = fig.add_subplot(1,1,1)
ax.plot(päevad, silu_andmed(aktsiad, n))
show()
