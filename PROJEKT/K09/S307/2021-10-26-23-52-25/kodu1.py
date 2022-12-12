from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(aList, x):
    c = 0
    b = len(aList)
    newlist = []
    a2 = []
    while True:
        if len(newlist) == b:
            break
        elif c < x - 1:
            a2.append(aList[c])
            newlist.append(harmonic_mean(a2))
            c += 1
        elif c <= b:
            a2 = aList[0:x]
            newlist.append(harmonic_mean(a2))
            aList.pop(0)
    return newlist
failinimi = input('Sisestage faili nimi')
f = open(failinimi + '.txt')
algandmed = f.readlines()
sorteeritud = []
f.close()
for element in algandmed:
    sorteeritud.append((element.split(',', 1)[1]).strip())
sorteeritud = [float(i) for i in sorteeritud]
plt.plot(sorteeritud, label = 'Enne silumist')
silutud = silu_andmed(sorteeritud, 50)
plt.xlabel('andmed')
plt.plot(silutud, label = 'Pärast silumist')
plt.legend()
plt.show()
    