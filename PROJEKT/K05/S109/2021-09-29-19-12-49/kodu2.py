import random
def suurväike(n):
    uus = ""
    punct = '!"
    punct1 = '!"
    i = 1
    for i in range(len(n)):
        if n[i].isupper():
            uus+= n[i].lower()
        elif n[i].islower():
            uus+= n[i].upper()
        elif n[i] in punct:
            uus+= random.choice(punct)
    print(uus)