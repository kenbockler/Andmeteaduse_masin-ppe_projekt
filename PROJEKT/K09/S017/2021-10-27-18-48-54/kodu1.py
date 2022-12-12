from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(j�rjend, t�isarv):
    uus_j�rjend = []
    i = 1
    arv = 1
    for el in j�rjend:
        if arv < t�isarv:
            lisa = harmonic_mean(j�rjend[0:i])
            arv += 1
        else:
            lisa = harmonic_mean(j�rjend[(i-t�isarv):i])
        uus_j�rjend += [lisa]
        i += 1
    return uus_j�rjend
f = open(input("Sisesta faili nimi: "))
andmed = []
kuup�evad = []
i = 0
for rida in f:
    tekst = rida.split(",")
    andmed += [float(tekst[1].strip("\n"))]
    i += 1
    kuup�evad += [i]
f.close()
silutud_andmed = silu_andmed(andmed, 50)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(kuup�evad, silutud_andmed, "-r", label="Silutud andmed")
ax.plot(kuup�evad, andmed, "-b", label="Andmed")
ax.set_ylim(0.0000, 0.0175)         
ax.set_xlim(0, 1000)
ax.legend()
plt.show()