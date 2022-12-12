from statistics import harmonic_mean
import matplotlib.pyplot as plt
import numpy as np
def silu_andmed(silutavad_andmed, mitu_el):
    andmed = silutavad_andmed.copy()
    prev_mean = 0
    data = []
    length = len(andmed)
    for i in range(length):
        if i + 1 >= mitu_el:
            k = mitu_el
        else:
            k = i + 1
        data.append(harmonic_mean(andmed[:k]))
        if i + 1 >= mitu_el:
            andmed.pop(0)
    return data
algandmed = input('Sisesta tekstifaili nimi: ')
silutavad_andmed = []
with open(algandmed, 'r') as f:
    andmed = [x.rstrip('\n') for x in f.readlines()]
for osa in andmed:
    rida = osa.split(',')
    silutavad_andmed.append(float(rida[1]))
silutud_andmed = silu_andmed(silutavad_andmed, 50)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(silutavad_andmed)
ax.plot(silutud_andmed)
plt.show()