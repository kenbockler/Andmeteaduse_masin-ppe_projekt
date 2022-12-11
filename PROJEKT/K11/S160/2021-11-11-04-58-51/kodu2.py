import numpy as np
maatriks = ([[4, 31],[2,6],[3,5],[8,7]])
def transponeeriK(x):
    uus = []
    x = np.fliplr(x)
    t_x = zip(*x)
    for rida in t_x:
        rida = rida[::-1]
        uus.append(rida)
    return uus
x = transponeeriK(maatriks)
