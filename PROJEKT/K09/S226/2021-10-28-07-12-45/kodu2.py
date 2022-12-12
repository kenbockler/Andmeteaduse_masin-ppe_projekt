import random
järjend = [11, 12, 13, 14, 15]
def minu_shuffle(järjend):
    for i in järjend:
        x = järjend.index(i)
        juhuslik_arv = random.randint(0, len(järjend) - 1)
        järjend[x] = järjend[juhuslik_arv]
        uus_list = []
print(minu_shuffle(järjend))