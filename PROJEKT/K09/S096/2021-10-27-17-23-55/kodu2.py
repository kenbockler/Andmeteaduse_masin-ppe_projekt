import random
def minu_shuffle(jrj):
    jrj2 = jrj[:]
    for i in range(len(jrj)):
        x = random.choice(jrj2)
        jrj[i] = x
        jrj2.remove(x)
a = [1, 3, 3, 4, 5, 5, 5, 6, 6]
print(a)
minu_shuffle(a)
print(a)