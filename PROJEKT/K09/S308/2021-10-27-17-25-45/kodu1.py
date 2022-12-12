from statistics import harmonic_mean
import matplotlib.pyplot as plt
nimi=input('Palun sisestage fail: ')
fail=open(nimi, 'r')
AllList= [line.strip() for line in fail]
ujukomaList=[]
w=0
pikkus=[]
for i in AllList:
    k=i.split(',')
    l=float(k[-1])
    ujukomaList.append(l)
    w=w+1
    pikkus.append(w)
def silu_andmed(ujukoma, n):
    new=[]
    uus=[]
    for a in ujukoma:
        new.append(a)
        uus.append(harmonic_mean(new))
        if len(new) == n:
            new.pop(0)
    ujukoma=uus
    return ujukoma
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(pikkus, ujukomaList, color="blue")
ax.plot(pikkus, silu_andmed(ujukomaList, 50), color="red")
plt.show()
fail.close()