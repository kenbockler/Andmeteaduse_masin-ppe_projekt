from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(järjend, n):
    jagajad = []
    uus_jär = []
    for i in range(len(järjend)):
        jagajad.append(järjend[i])
        if len(jagajad) > n:
            jagajad.pop(0)
        har_keskmine = harmonic_mean(list(map(float, jagajad)))
        uus_jär.append(har_keskmine)
    return uus_jär
sisend = input("Sisestage faili nimi: ")
f = open(sisend)
hinnad = []
päevade_arv = 0
päevade_arv_jär = []
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
