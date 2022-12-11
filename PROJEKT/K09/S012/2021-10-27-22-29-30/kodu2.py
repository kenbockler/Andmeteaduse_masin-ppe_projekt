import random
def minu_shuffle(a):
    for i in a:
        b = random.choice(a)
        a.append(b)
        a.remove(b)
    