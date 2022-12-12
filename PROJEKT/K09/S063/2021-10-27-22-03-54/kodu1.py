from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(järjend, n):
    j = järjend[:]
    uus_j = []
    for i in range(len(j)):
        if len(j[:i+1]) < n:
            uus_j.append(harmonic_mean(j[:i+1]))
        else:
            jada = list()
            for k in range(n-1, -1, -1):
                jada = jada + [j[i-k]]
            uus_j.append(harmonic_mean(jada))
    return uus_j
faili_nimi = input('Sisestage aktsia hindade failinimi: ')
f = open(faili_nimi, 'r')
aktsiad = list()
for rida in f:
    rida = rida.split(',')
    aktsiad.append(float(rida[1].strip()))
f.close()
keskmistatud = silu_andmed(aktsiad, 50)
plt.title("Aktsia hindade keskmistamine")
plt.grid()
plt.plot(aktsiad, label='algandmed')
plt.plot(keskmistatud, label='silutud andmed')
plt.legend(loc='best')
plt.show()
