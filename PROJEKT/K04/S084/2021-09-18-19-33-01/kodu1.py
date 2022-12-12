from math import *
def koogi_hind(nimi, mõõt):
    if nimi == "šokolaadikook":
        hind = pi * mõõt * mõõt * 0.06
    elif nimi == "ploomikook":
        hind = pi * mõõt * mõõt * 0.04
    elif nimi == "Napoleoni kook":
        hind = mõõt * mõõt * 0.10
    else: 
        raise Exception("Sellist kooki andmebaasist ei leitud")
    return round(hind, 2)
while True:
    koogi_nimi = input("Sisesta koogi nimi: ")
    if koogi_nimi == "":
        break
    try:
        koogi_mõõt = float(input("Sisesta koogi mõõt: "))
    except:
        print("Koogimõõt peab olema numbrites")
        continue
    print(f"{koogi_nimi} maksab {koogi_hind(koogi_nimi, koogi_mõõt)} eurot.")