from math import *
def koogi_hind(koogi_nimi, mõõt):
    if koogi_nimi == "šokolaadikook":
        return round(0.06 * (mõõt**2 * pi), 2)
    elif koogi_nimi == "ploomikook":
        return round(0.04 * (mõõt**2 * pi), 2)
    elif koogi_nimi == "Napoleoni kook":
        return round(0.1 * (mõõt**2), 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
kook = input("Sisesta koogi nimi: ")
while kook != "":
    koogi_mõõt = float(input("Sisesta koogi mõõt: "))
    print(koogi_hind(kook, koogi_mõõt))
    kook = input("Sisesta koogi nimi: ")