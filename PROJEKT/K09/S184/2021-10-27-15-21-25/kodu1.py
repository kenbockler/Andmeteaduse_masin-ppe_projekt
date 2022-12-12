from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(c,n):
    uus=[]
    for i in range(1,len(c)+1):
        if i<=n:
            harmo=c[0:i]
        else:
            c.pop(0)
            harmo=c[0:n]
        h=harmonic_mean(harmo)
        uus.append(h)
    return uus
f1="aktsiad.txt"
f=open(f1, encoding="UTF-8")
a=f.readlines()
f.close
n=int(50)
c=[]
for i in a:
    d=i.strip("\n").split(",")
    if d==[""]:
        break
    else:
        b=float(d[-1].strip())
        c.append(b)
toorandmed=c.copy()
uus1=silu_andmed(c,n)
fig = plt.figure()
plt.title("Aktsiad") 
ax = fig.add_subplot(1,1,1)
ax.plot(toorandmed)
ax.plot(uus1)    
plt.show() 
