from math import pi
s = 0.06
p = 0.04
n = 0.1
while True:
    kooginimi = input("Mis on koogi nimi?")
    if kooginimi == "":
        break
    mõõt = float(input("Kui suur on koogi külg või raadius sentimeetrites?"))
    def koogi_hind(kooginimi, mõõt):
        def pindala(mõõt):
            ruut = mõõt*mõõt
            ring = pi*mõõt*mõõt
            if kooginimi == "Napoleoni kook":
                return ruut
            elif kooginimi == "ploomikook" or "šokolaadikook":
                return ring
        sokokook = round(pindala(mõõt)*s, 2)
        plookook = round(pindala(mõõt)*p, 2)
        napokook = round(pindala(mõõt)*n, 2)
        if kooginimi == "Napoleoni kook":
            return napokook
        elif kooginimi == "ploomikook":
            return plookook
        elif kooginimi == "šokolaadikook":
            return sokokook
    x = koogi_hind(kooginimi, mõõt)
    if kooginimi == "Napoleoni kook" or "ploomikook" or "šokolaadikook":
         x = koogi_hind(kooginimi, mõõt) and print(x)
    if kooginimi != "Napoleoni kook" and kooginimi != "ploomikook" and kooginimi != "šokolaadikook":
        raise Exception("Sellist kooki andmebaasist ei leitud")
