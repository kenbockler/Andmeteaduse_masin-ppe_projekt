import random
def minu_shuffle(jar):
    for i in range(len(jar)):
        ran_i = random.randint(0, len(jar)-1)
        jar[i], jar[ran_i] = jar[ran_i], jar[i]
    