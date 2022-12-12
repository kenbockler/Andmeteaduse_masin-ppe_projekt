import random
a = [1, 2]
def minu_shuffle(x):
    pikkus=len(x)
    uus_järjend = []
    juhuslik_jada = random.sample(range(0,pikkus),pikkus)
    for i in range(0,pikkus):
        vana_järjendi_el = a[juhuslik_jada[i]]
        uus_järjend.append(vana_järjendi_el)
    return(uus_järjend)
print(minu_shuffle(a))