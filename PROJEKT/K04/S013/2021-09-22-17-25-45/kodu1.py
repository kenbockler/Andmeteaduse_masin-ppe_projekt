from math import pi
def koogi_hind(nimi, m��t):
    if nimi == "�okolaadikook":
        hind = 0.06
        pindala = pi * float(m��t)**2
        return round(hind*pindala, 2)
    elif nimi == "ploomikook":
        hind = 0.04
        pindala = pi * float(m��t)**2
        return round(hind*pindala, 2)
    elif nimi == "Napoleoni kook":
        hind = 0.10
        pindala = (float(m��t)**2)
        return round(hind*pindala, 2)
    else:
        print("Sellist kooki andmebaasist ei leitud")
x = True
while x:
    nimi = input("Sisesta koogi nimi: ")
    if nimi == "":
        break
    else:
        m��t = input("Sisesta koogi m��t: ")
        print("Koogi hind on ", koogi_hind(nimi, m��t), "eurot.")
    