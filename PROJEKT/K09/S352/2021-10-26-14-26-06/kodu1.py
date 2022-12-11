import matplotlib.pyplot as plt
from statistics import harmonic_mean
def silu_andmed(andmed,n):
    keskmistatud_andmed=[]
    if len(andmed)>=n:
        for i in range(len(andmed)+1):
            if i < n:
                keskmistatud_andmed.append(harmonic_mean(andmed[:i+1]))
            elif i>n:
                keskmistatud_andmed.append(harmonic_mean(andmed[i-n:i]))
        return keskmistatud_andmed
    elif len(andmed)<n:
        for i in range(len(andmed)):
            keskmistatud_andmed.append(harmonic_mean(andmed[:i+1]))
        return keskmistatud_andmed
f=open("aktsiad.txt","r")
andmed=f.read().split("\n")
f.close()
hinnad=[]
for el in andmed:
    el=el.split(",")
    hinnad.append(float(el[1]))
päev=list(range(0,len(hinnad)))
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(päev, hinnad, "-")
ax.set_xlabel("Aeg (päevades)")
ax.set_ylabel("Aktsia hind")
ax.plot(päev,silu_andmed(hinnad,50),"-")
plt.show()
