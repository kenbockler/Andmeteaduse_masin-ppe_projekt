from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(järjend, n):
    järjend.reverse()
    avg2 = []
    for i in range(len(järjend)): 
        if i == len(järjend):
            avg2.append(järjend[i])
        else:
            avg = float(harmonic_mean(järjend[i:i+n]))
            avg2.append(avg)
    järjend.reverse()
    avg2.reverse()
    return avg2
f = open("aktsiad.txt")
read = []
kuupäev = []
hind = []
for rida in f:
    r1 = rida.strip().split()
    read.append(r1)
    kuupäev.append(r1[0:3])
    hind.append(float(r1[3]))
f.close()
silutud_hinnad = silu_andmed(hind, 50)
indeksid = []
for i in range(len(hind)):
    indeksid.append(i)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(indeksid, hind)
ax.plot(indeksid, silutud_hinnad)
plt.show()
