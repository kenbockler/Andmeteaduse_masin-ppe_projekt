from random import randint
def suurv�ike(sisend):
    kirjavahem�rgid='!"
    vastus = ("")
    rnd = randint(0,len(kirjavahem�rgid))
    m�rk = kirjavahem�rgid[rnd]             
    for el in sisend:
        if el.islower():
            vastus += el.upper()
        else:
            if el.isupper():
               vastus += el.lower()
            elif el in kirjavahem�rgid:
                vastus +=m�rk
            else:
                vastus+=el
    return vastus
