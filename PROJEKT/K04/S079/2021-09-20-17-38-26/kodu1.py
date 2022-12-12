from math import pi
def koogi_hind(koogi_nimi, koogi_mõõt):
    if koogi_nimi == "šokolaadikook":
        hind = round(pi * koogi_mõõt**2 * 0.06, 2)
        return hind
    if koogi_nimi == "ploomikook":
        hind = round(pi * koogi_mõõt**2 * 0.04, 2)
        return hind
    if koogi_nimi == "Napoleoni kook":
        hind = round(koogi_mõõt**2 * 0.10, 2)
        return hind
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
nimi = input("Sisesta koogi nimi (või lõpetamiseks Enter): ")
while True:
    if nimi == "":
        break
    else:
        mõõt = float(input("Sisesta koogi mõõt: "))
        print(koogi_hind(nimi, mõõt))
        nimi = input("Sisesta koogi nimi (või lõpetamiseks Enter): ")