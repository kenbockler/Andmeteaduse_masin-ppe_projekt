import random
def minu_shuffle(järjend):
    for i in range(len(järjend)-1, 0, -1):
        j = random.randint (0, i + 1)
        järjend[i], järjend[j] =  järjend[j], järjend[i]
    