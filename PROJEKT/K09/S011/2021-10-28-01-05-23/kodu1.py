from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(j�rjend, mitme_kaupa):
    a = j�rjend
    b = []
    x = 0
    while x <= mitme_kaupa:
        for el in a:
            Harmooniline_keskmine = [harmonic_mean(el)]
            b = b + Harmooniline_keskmine
            x +=1
    return (b)
andmed = open(input("Sisesta faili nimi: "))
arv = int(input("Sisesta mitme kaupa keskmistada: "))
andmed_j�r = []
for rida in andmed_j�r:
     kuup�eva_andmed = [(rida.split(","))]
     andmed_j�r = andmed_j�r +  kuup�eva_andmed[1]
silutud = silu_andmed(andmed_j�r, arv)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(andmed_j�r, silutud)
plt.show()