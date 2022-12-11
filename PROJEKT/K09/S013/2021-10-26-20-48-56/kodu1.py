from statistics import harmonic_mean
import matplotlib.pyplot as plt
f=input("Sisesta faili nimi")
fail=open(f,"r", encoding="UTF-8")
j�rjend= []
for rida in fail:
    rida=rida.strip("\n")
    rida=rida.split(",")
    j�rjend.append(float(rida[1]))
def silu_andmed(a,b):
    silutud_j�rjend= []
    lisaj�rjend = []
    for rida in a:
        lisaj�rjend.append(rida)
        if len(lisaj�rjend) > b:
            lisaj�rjend.pop(0)
        silutud_j�rjend.append(harmonic_mean(lisaj�rjend))
    return silutud_j�rjend
fig= plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(j�rjend)
ax.plot(silu_andmed(j�rjend,50))
plt.show()
fail.close()