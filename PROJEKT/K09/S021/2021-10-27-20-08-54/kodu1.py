from statistics import harmonic_mean
import matplotlib.pyplot as plt
nimi = str(input("Palun sisestage faili nimi: "))
n = int(input("Sisestage t�isarvuline n v��rtus: "))
f = open(nimi,"r", encoding = "UTF-8")
hinnaj�rjend = []
for rida in f:
    j�rjend = rida.strip().split()
    hind = [float(j�rjend.pop())]
    hinnaj�rjend += hind
def silu_andmed(j�rjend, t�isarv):
    keskmistatudj�rjend = []
    for indeks in range(1, len(j�rjend) + 1):
        algus = max(0, indeks - t�isarv)
        h_keskmine = harmonic_mean(j�rjend[algus:indeks])
        keskmistatudj�rjend += [h_keskmine]
    return keskmistatudj�rjend
plt.plot(hinnaj�rjend)
plt.plot(silu_andmed(hinnaj�rjend, n))
plt.show()
