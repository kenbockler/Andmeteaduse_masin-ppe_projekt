from statistics import harmonic_mean
import matplotlib.pyplot as plt
f = input("Sisesta failinimi: ")
f = open(f, "r")
w =f.read()
w = w.strip()
w = w.split("\n")
kuup�evad = []
arvud =[]
for i in range(len(w)):
    w[i] = w[i].split(",")
    kuup�evad.append(w[i][0])
    arvud.append(float(w[i][1]))
f.close()
def silu_andmed(x,n):
    keskmistamine = []
    uus_j�rjend = []
    for i in range(len(x)):
        if len(keskmistamine) < n:
            keskmistamine.append(x[i])
        else:
            keskmistamine.pop(0)
            keskmistamine.append(x[i])  
        harmooniline = harmonic_mean(keskmistamine)
        uus_j�rjend.append(harmooniline)
    return uus_j�rjend
silutud = silu_andmed(arvud, 50)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)  
ax.plot(range(len(kuup�evad)), arvud)  
ax.plot(range(len(kuup�evad)), silutud)
plt.show() 
