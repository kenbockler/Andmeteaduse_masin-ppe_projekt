import matplotlib.pyplot as plt
from statistics import harmonic_mean
f = open("aktsiad.txt")
read = f.readlines()
hinnad = []
for rida in read:
    aktsiad = rida.strip().split(", ")
    hinnad.append(float(aktsiad[1]))
print(hinnad)
f.close()
def silu_andmed(algandmed, n):
    tulemused = [] 
    n_elementi = [] 
    for el in algandmed:
        n_elementi.append(el)
        if len(n_elementi) > n:
            del(n_elementi[0])
        tulemused.append(float(harmonic_mean(n_elementi)))
    return tulemused
silutud = silu_andmed(hinnad, 50)
plt.plot(hinnad, label = "algandmed")
plt.plot(silutud, label = "silutud")
plt.legend()
plt.show()
    