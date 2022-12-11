from math import pi
def koogi_hind(koogi_nimi, koogi_moot):
    S_ring = koogi_moot ** 2 * pi
    S_ruut = koogi_moot ** 2
    sokolaadikoogi_hind = 0.06
    ploomikoogi_hind = 0.04
    napoleonikoogi_hind = 0.10
    if koogi_nimi == "šokolaadikook":
        return round(sokolaadikoogi_hind * S_ring, 2)
    elif koogi_nimi == "ploomikook":
        return round(ploomikoogi_hind * S_ring, 2)
    elif koogi_nimi == "napoleonikook":
        return round(napoleonikoogi_hind * S_ruut, 2)
    else:
        raise Exception("Sellist kooki andmebaasist ei leitud")
while True:
    nimi = str(input("Koogi nimi: ")).lower().replace(" ","")
    if nimi == "":
        break
    else:
        moot = float(input("Koogi pikkus/raadius: "))
    hind = koogi_hind(nimi, moot)
    print(hind)
    continue