from statistics import harmonic_mean
import matplotlib.pyplot as plt
nimi= input("Sisesta algfaili nimi: ")
andmed=[]
with open(nimi ,"r") as f:
    read = f.read().splitlines()
    for rida in read:
        li = rida.split(",")
        andmed.append(float(li[1])) 
f.close()
def silu_andmed(andmed, n):
    tulemus = []
    for x in range(len(andmed)) :
        jarg =[]
        a=0
        while a<n and x-a>-1:
            jarg.append(float(andmed[x-a]))
            a+=1
        tulemus.append(harmonic_mean(jarg))
    return(tulemus)
silu_andmed(andmed, n)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(andmed, tulemus)
plt.show()     
