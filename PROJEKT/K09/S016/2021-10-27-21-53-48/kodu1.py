def silu_andmed(j�rjend, n):
    outputj�rjend = []
    for indeks in range(1, len(j�rjend) + 1):
        algus = max(0,indeks - n)
        arvutus = harmonic_mean(j�rjend[algus: indeks])
        outputj�rjend += [arvutus]
    return outputj�rjend
j = []
j1 = input("Sisesta j�rjend: ").strip("[").strip("]"). strip("\n").split(",")
for el in j1:
    j += [float(el)]
print(j)
from statistics import *
outputj�rjend = []
n = int(input("Sisesta n-i v��rtus: "))
import matplotlib.pyplot as plt
plt.plot(j1)
plt.plot(silu_andmed(j,n))
plt.show()