from math import pi
def koogi_hind(nimi, m��t):
    if nimi == "�okolaadikook":
        m��t1 = pi * m��t ** 2
        hind1 = m��t1 * 0.06
        hind_l�pp1 = round(hind1, 2)
        return hind_l�pp1
    elif nimi == "ploomikook":
        m��t2 = pi * m��t ** 2
        hind2 = m��t2 * 0.04
        hind_l�pp2 = round(hind2, 2)
        return hind_l�pp2
    elif nimi == "Napoleoni kook":
        m��t3 = m��t ** 2
        hind3 = m��t3 * 0.10
        hind_l�pp3 = round(hind3, 2)
        return hind_l�pp3
    else:
        raise Exception("Sellist kooki andmebaasis ei leidu")
nimi = input("Sisesta soovitava koogi nimi: ")
m��t = float(input("Sisesta soovitava koogi m��t: "))
try:
    l�pphind = koogi_hind(nimi, m��t)
    print("Teie koogi l�pphind on: ", l�pphind, "eurot.")
except:
    print("Sellist kooki andmebaasist ei leitud")
