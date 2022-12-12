from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(jrj, n):
    silutud = []
    keskmista = []
    for i in range(len(jrj)):
        if len(keskmista) < n:
            keskmista.append(jrj[i])
        else:
            keskmista.pop(0)
            keskmista.append(jrj[i])
        silutud.append(round(harmonic_mean(keskmista), 6))
    return silutud
f = open("aktsiad.txt", encoding="UTF-8")
aktsiad = []
for rida in f:
    päev, hind = rida.strip().split(",")
    aktsiad.append(float(hind))
f.close()
keskmistatud_aktsiad = silu_andmed(aktsiad, 50)
päevad = list(range(1, len(aktsiad)+1))
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(päevad, aktsiad)
ax.plot(päevad, keskmistatud_aktsiad)
ax.set_label("päevad")
plt.show()
