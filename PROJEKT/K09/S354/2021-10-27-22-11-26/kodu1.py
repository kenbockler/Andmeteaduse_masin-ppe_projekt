import matplotlib.pyplot as plt
def silu_andmed(a, n):
    b = []
    p_d = 0
    for i in range(len(a)):
        pod_d = 1/a[i]
        if i + 1 > n:
            p_d += pod_d
            p_d = p_d - 1/a[(i-n)]
        else:
            p_d += pod_d
        if (i+1) <= n:
            result = (i+1) / p_d
        else:
            result = n / p_d
        b += [result]
    return b
f = open('aktsiad.txt')
aktsiad = []
kogum = []
k = 0
for rida in f:
    rida = rida.strip()
    rida = rida.split()
    aktsiad += [float(rida[3])]
f.close()
aktsia_s = silu_andmed(aktsiad, 50)
for m in range(len(aktsiad)):
    k += 1
    kogum += [k]
kuud         = kogum
sissetulekud = aktsiad
väljaminekud = aktsia_s
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(kuud, sissetulekud)
ax.plot(kuud, väljaminekud)
plt.show()