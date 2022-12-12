import string, random
def suurväike(sone):
    i = 0
    uus = list(sone)
    lopp = ""
    for el in uus:
        if el.isupper():
            uus[i] = el.lower()
        elif el.islower():
            uus[i] = el.upper()
        else:
            if el not in string.punctuation:
                uus[i] = el
            else:
                suva = random.randint(0, 32)
                sone = sone.replace(el, string.punctuation[suva])
                uus[i] = sone[i]
        i+=1
    return (lopp.join(uus))