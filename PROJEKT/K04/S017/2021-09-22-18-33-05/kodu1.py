from math import pi
while True:
    nimi = input("Millist kooki tahad? (�okolaadikook, ploomikook v�i Napoleoni kook) ")
    if nimi == "":
        break
    m��t = float(input("Kui suurt kooki tahad? (cm) "))
    def koogi_hind(nimi, m��t):
        if nimi == "�okolaadikook":
            return round(0.06 * m��t * m��t * pi, 2)
        elif nimi == "ploomikook":
            return round(0.04 * m��t * m��t * pi, 2)
        elif nimi == "Napoleoni kook":
            return round(0.10 * m��t * m��t, 2)
        else:
            raise ValueError("Sellist kooki andmebaasist ei leidu")
    print("Selle koogi hind on", koogi_hind(nimi, m��t))
    