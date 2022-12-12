from random import randint
def suurväike(sone):
    string = '!"
    a = randint(0, len(string))
    a = string[a]
    vastus = ''
    for i in range(len(sone)):
        x = sone[i]
        if x in string:
            vastus += a
        elif x.lower() == x:
            vastus += x.upper()
        else:
            vastus += x.lower()
    return vastus
            