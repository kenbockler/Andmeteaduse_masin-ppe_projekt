from copy import *
def rek_abs(j):
    uus_j = []
    for el in j:
        if isinstance(el, list) == False:
            uus_j += [abs(el)]
        if isinstance(el, list) == True:
            uus_j += [rek_abs(el)]
    return uus_j