from math import pi
def koogi_hind(nimi,m��t) :
    if nimi != str(�okolaadikook) or nimi != str(ploomikook) or nimi != str(Napoleoni_kook) :
        raise Exception("Sellist kooki andmebaasist ei leitud")
    elif nimi == �okolaadikook :
        �okolaadikook = float(0.06)
        return round((nimi*(m��t**2)*3.14),2)
    elif nimi == ploomikook :
        ploomikook = float(0.04)
        return round((nimi*(m��t**2)*3.14),2)
    elif nimi == Napoleoni_kook :
        Napoleoni_kook = float(0.10)
        return round(m��t**2,2)
while True:
    nimi = input("Millist kooki soovite osta? ")
    if nimi == "":
        break
    else:
        m��t = float(input("Koogi m��t (kas raadius v�i k�lje pikkus): "))
        print("Koogi hind on ", koogi_hind(nimi,m��t), "�")