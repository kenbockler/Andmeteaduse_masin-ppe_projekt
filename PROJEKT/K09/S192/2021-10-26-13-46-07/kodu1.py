from statistics import harmonic_mean
def silu_andmed(algandmed, täisarv):
    uued_andmed = []
    H = []
    j = 1
    i = 0
    for element in algandmed:
        if j <= täisarv:
            H.append(element)
            uued_andmed.append(harmonic_mean(H))
            j += 1
        elif j > täisarv:
            H.pop(0)
            H.append(algandmed[i+täisarv])
            uued_andmed.append(harmonic_mean(H))
            i += 1
    return uued_andmed
import matplotlib.pyplot as plt
fail = input('Sisesta failinimi: ')
r = open(fail, 'r')
andmed = []
andmete_arv = []
i = 1
for read in r:
    read = read.strip().split(',')
    hind = float(read[1])
    andmed.append(hind)
    andmete_arv.append(i)
    i += 1
harm_k = silu_andmed(andmed, 50)
r.close()
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(andmete_arv, andmed)
ax.plot(andmete_arv, harm_k)
plt.show()
    