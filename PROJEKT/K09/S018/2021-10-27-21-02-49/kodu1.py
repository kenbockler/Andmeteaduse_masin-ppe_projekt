from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(j�rjend,t�isarv):
    silutud = []
    n_viimast = []
    for i in range(len(j�rjend)):
        if len(n_viimast) < t�isarv:
            n_viimast.append(j�rjend[i])
        else:
            n_viimast.append(j�rjend[i])
            n_viimast.pop(0)
        silutud.append(harmonic_mean(n_viimast))
    return silutud
faili_nimi = input("Sisesta faili nimi: ")
n = int(input("Sisesta n: "))
arvud = []
kuup�evad = []
with open(faili_nimi, "r", encoding="UTF-8") as f:
    j�rjend = f.read().replace("\n", ", ").split(", ")
    for i in range(0,len(j�rjend),2):
        kuup�evad.append(j�rjend[i])
        arvud.append(float(j�rjend[i+1]))
silutud = silu_andmed(arvud, n)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(kuup�evad, arvud, label="Aktsia hind")
ax.plot(kuup�evad, silutud, label="Aktsia hind silutult")
ax.set_xlabel("Kuup�evad")
ax.set_ylim(0, 0.03)
ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])
ax.legend()
plt.show()