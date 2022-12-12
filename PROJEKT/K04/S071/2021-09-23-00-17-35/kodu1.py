from math import *
def koogi_hind(nimi,mõõt):
    if nimi == "šokolaadikook":
        raadius = mõõt
        hind = (pi * (raadius * raadius)) * 0.06
    elif nimi =="ploomikook":
        raadius = mõõt
        hind = (pi * (raadius * raadius)) * 0.04
    elif nimi == "Napoleoni kook":
        küljepikkus = mõõt
        hind = (küljepikkus * küljepikkus) * 0.10
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
    return(round(hind,2))
nimiNOPE = ""
while True:
    nimi = input("Koogi nimi: ")
    if nimi == nimiNOPE:
        break
    else:
        mõõt = float(input("Koogi mõõt: "))
        print(koogi_hind(nimi,mõõt))
