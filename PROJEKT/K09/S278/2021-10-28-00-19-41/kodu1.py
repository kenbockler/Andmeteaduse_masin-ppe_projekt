from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(järjend, n):
    uus_järjend = []
    for indeks in range(1, len(järjend) + 1):
        algus = max(0, indeks - n)
        jagaja = harmonic_mean(järjend[algus:indeks])
        uus_järjend += [jagaja]
    return(uus_järjend)
aktsiad = []
aktsiad2 = []
file = open((input('Sisesta palun faili nimi:')),"r")
for data in file:
    data = data.strip()
    data = data.split()
    aktsiad = aktsiad + [float(data[3])]
file.close
täpselised_aktsiad = silu_andmed(aktsiad, 50)
plt.plot(aktsiad)
plt.plot(täpselised_aktsiad)
plt.xlabel("Aktsiate arv")
plt.ylabel("Aktsiad")
plt.show()
