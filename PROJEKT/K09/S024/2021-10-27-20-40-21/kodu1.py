from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(j�rjend, n):
    jagajad = []
    uus_j�r = []
    for i in range(len(j�rjend)):
        jagajad.append(j�rjend[i])
        if len(jagajad) > n:
            jagajad.pop(0)
        har_keskmine = harmonic_mean(list(map(float, jagajad)))
        uus_j�r.append(har_keskmine)
    return uus_j�r
sisend = input("Sisestage faili nimi: ")
f = open(sisend)
hinnad = []
p�evade_arv = 0
p�evade_arv_j�r = []
for rida in f:
    rida = rida.strip().split()
    hinnad.append(float(rida[3]))
silutud_andmed = silu_andmed(hinnad, 50)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(hinnad, label="Aktsiate hinnad")
ax.plot(silutud_andmed, label="Silutud andmed")
ax.set_xlabel("Aktsiate muutus aastatega")
ax.legend()
plt.show()
