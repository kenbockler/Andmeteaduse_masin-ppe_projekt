from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(lst,taisarv):
    end_lst =[]
    for i in range(len(lst)):
        if i< taisarv:
            end_lst += [harmonic_mean(lst[:i+1])]
        else:
            end_lst += [harmonic_mean(lst[i-taisarv:i])]
    return end_lst
kuud = []
saktsiad = []
f = open("aktsiad.txt","r")
for rida in f:
    a = rida.strip("\n").split(", ")
    aktsiad += [float(a[1])]
    kuud += [a[0]]
f.close()
sissetulekud = [710, 1200, 1445, 1690, 1350, 1223, 1470, 1200, 808, 698]
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(kuud, aktsiad)
ax.set_xticks([0,200,400,600,800,1000])
plt.show()    