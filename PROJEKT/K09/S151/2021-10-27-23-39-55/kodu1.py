from statistics import harmonic_mean
import matplotlib.pyplot as plt
f = open("aktsiad.txt")
hind = []
for rida in f:
    aktsia = rida.strip("\n").split(",")
    hind.append(float(aktsia[1]))
f.close()
pikkus = len(hind)
punkte = list(range(1, pikkus + 1))
def silu_andmed(jär, mitu):
    silutud = []
    arvuta = []
    n = 0
    for i in range(len(jär)):
        n += 1
        arvuta.append(jär[i])
        if n > mitu:
            del arvuta[0:(mitu-(mitu-1))]
            silutud.append(harmonic_mean(arvuta))
        else:
            silutud.append(harmonic_mean(arvuta))
    return silutud
harm = silu_andmed(hind, 50)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(punkte, hind)
ax.plot(punkte, harm)
ax.set_ylabel("Aktsia turuväärtus")
plt.show()
