from math import pi
def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        S = pi * mõõt ** 2
        hind = S * 0.06
        return round(hind, 2)
    elif nimi == "ploomikook":
        S = pi * mõõt ** 2
        hind = S * 0.04
        return round(hind, 2)
    elif nimi == "Napoleoni kook":
        S = mõõt ** 2
        hind = S * 0.1
        return round(hind, 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
while True:
    nimi = input("Sisestage koogi nimi: ")
    if nimi == "":
        break
    mõõt = float(input("Sisestage koogi mõõt sentimeetrites: "))
    print("Koogi hind on " + str(koogi_hind(nimi, mõõt)) + " eurot.")