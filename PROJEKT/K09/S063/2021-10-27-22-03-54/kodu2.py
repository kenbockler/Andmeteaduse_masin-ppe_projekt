import random
def minu_shuffle(järjend):
    for i in range(len(järjend)):
        while True:
            rnd_i = random.choice(range(len(järjend)))
            if rnd_i != i:
                el = järjend[i]
                järjend[i] = järjend[rnd_i]
                järjend[rnd_i] = el
                break
    return järjend
