from statistics import harmonic_mean
import matplotlib.pyplot as plt
f = open(input("Sisestage faili nimi: "), "r+", encoding = "UTF-8")
l�pp_j�r =[]
l�pp_j�r2 = []
p�evad = []
n = 0
maatriks = f.read().split("\n")
for andmed in maatriks:
    vajalik = andmed.split(",")[1]
    l�pp_j�r.append(vajalik)
    n += 1
    p�evad.append(n)
def silu_andmed(j�rjend, number):
    uus = list(map(float, j�rjend))
    for n in len(uus):
        uude = harmonic_mean(uus[n:(number+n)])
        l�pp_j�r2.append(uude)
    return l�pp_j�r2
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_ylim(0, 0.0175)
ax.set_xticks([0,200,400,600,800,1000])
ax.plot(p�evad, l�pp_j�r, "o-", label="Algandmed")
ax.plot(p�evad, l�pp_j�r2, "^-r", label="Silutud andmed")
ax.set_xlabel("P�evad")
plt.show()           
    