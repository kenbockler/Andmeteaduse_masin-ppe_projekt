from math import pi
while True:
    nimi=input("Sisestage soovitava koogi nimi: ")
    if nimi=="":
        break
    m��t=float(input("Sisestage soovitava koogi raadius/k�ljepikkus: "))
    def koogi_hind(nimi, m��t):
        if nimi !="�okolaadikook" and nimi!="ploomikook" and nimi!="Napoleoni kook":
            raise Exception("Sellist kooki andmebaasist ei leitud")
        if nimi=="�okolaadikook":
            hind=0.06*pi*m��t**2
        if nimi=="ploomikook":
            hind=0.04*pi*m��t**2
        if nimi=="Napoleoni kook":
            hind=0.1*m��t**2
        return round(hind, 2)
    maksumus=koogi_hind(nimi, m��t)
    print("Koogi hind on " + str(maksumus) + " eurot.")
    