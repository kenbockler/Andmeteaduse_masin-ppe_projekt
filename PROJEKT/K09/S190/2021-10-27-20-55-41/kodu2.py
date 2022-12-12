from random import randint
def minu_shuffle(järjend):
    for i in range(len(järjend)**2):
        a = järjend.pop(randint(0,len(järjend)-1))
        järjend.insert(len(järjend),a)
