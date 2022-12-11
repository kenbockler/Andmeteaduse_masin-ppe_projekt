from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(j�rjend, n):
    i = 0
    j�r = []
    for i in range(len(j�rjend)):
        if i == 0:
            a = [j�rjend[i]]
            j�r.append(float(harmonic_mean(a)))
            i += 1
        elif i >= n-1:
            b = j�rjend[i-(n-1):i-(n-1)+n]
            j�r.append(float(harmonic_mean(b)))
            i += 1
        elif 0 < i < n-1:
            c = j�rjend[0:i+1]
            j�r.append(float(harmonic_mean(c)))
    return j�r
f = open(input('Sisesta faili nimi: '))
aktsiad = []
for rida in f:
    aktsiad.append(float(rida.strip('\n').split(', ')[1]))
plt.plot(aktsiad)
plt.plot(silu_andmed(aktsiad, 50))
plt.show()
f.close()