from math import *
def koogi_hind(nimi, m��t):
    if nimi == "�okolaadikook":
        return round(pi*(m��t**2)*0.06, 2)
    elif nimi =="ploomikook":
        return round(pi*(m��t**2)*0.04, 2)
    elif nimi == "Napoleoni kook":
        return round(m��t**2*0.1, 2)
    else:
        raise ValueError("Sellist kooki andmebaasist ei leidu")
while True:
    koogi_nimi = str(input("Sisestage koogi nimi: "))
    if koogi_nimi == "":
        break
    else:
        suurus = float(input("Sisestage koogi m��t: "))
        tulemus=koogi_hind(koogi_nimi, suurus)
    print("Koogi hind on" , tulemus , "eurot")
    continue
