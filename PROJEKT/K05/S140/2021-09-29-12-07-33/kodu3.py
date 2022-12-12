from math import floor
def suur_karp(suur, kogus):
    suhe = kogus / 5
    if suur < suhe:
        suhe = suur
    return floor(suhe)
def moos(suur, väike, kogus):
    uus_kogus = kogus - 5 * suur_karp(suur, kogus)
    if uus_kogus <= väike:
        väike = uus_kogus
    else:
        return -1
    return suur_karp(suur, kogus) + väike
