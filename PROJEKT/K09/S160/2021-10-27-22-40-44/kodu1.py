from statistics import harmonic_mean
import matplotlib.pyplot as plt
andmed_aktsia = open(input("Sisestage uuritav fail: "))
n = 50
jarjend = []
jarjend2 = jarjend
for data in andmed_aktsia: 
    hind = data.split(' ')
    hind = hind[-1]
    hind = hind.split('\n')
    hind = hind[0]
    hind = float(hind)
    hind = jarjend.append(hind)
for indeks in range(1, len(jarjend) + 1):
     algus = max (0, indeks - n)
     (jarjend[algus:indeks])
for indeks in range(1, len(jarjend2) + 1):
    calculus =(0, n/(1/indeks))
    (jarjend[calculus:indeks])
muutmata = jarjend
plt.plot(muutmata)
print(muutmata)
plt.show()
andmed_aktsia.close()