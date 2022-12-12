from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(hinnad, n):
    listi_pikkus = len(hinnad)
    i = 1
    vahej�rj = []
    keskmine = []
    while True:
        if i <= n:
            vahej�rj.append(hinnad[i-1])
            a = harmonic_mean(vahej�rj)
            keskmine.append(a)
            i += 1
        elif i > n and i <= listi_pikkus:
            vahej�rj.append(hinnad[i-1])
            vahej�rj.remove(vahej�rj[0])
            a = harmonic_mean(vahej�rj)
            keskmine.append(a)
            i += 1
        else:
            break
    return keskmine
fail = open(input("Sisesta andmete faili nimetus: "))
hinnad = []
ridade_arv = []
i = 0
for rida in fail:
    i += 1
    ridade_arv.append(i)
    a = rida.strip().split(", ")
    hinnad.append(float(a[1]))
fail.close()
keskmine = silu_andmed(hinnad, 50)
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(ridade_arv, hinnad)
ax.plot(ridade_arv, keskmine)
plt.show()
        