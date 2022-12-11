def silu_andmed(järjend, n):
    outputjärjend = []
    for indeks in range(1, len(järjend) + 1):
        algus = max(0,indeks - n)
        arvutus = harmonic_mean(järjend[algus: indeks])
        outputjärjend += [arvutus]
    return outputjärjend
j = []
j1 = input("Sisesta järjend: ").strip("[").strip("]"). strip("\n").split(",")
for el in j1:
    j += [float(el)]
print(j)
from statistics import *
outputjärjend = []
n = int(input("Sisesta n-i väärtus: "))
import matplotlib.pyplot as plt
plt.plot(j1)
plt.plot(silu_andmed(j,n))
plt.show()