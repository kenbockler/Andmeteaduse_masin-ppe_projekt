from math import pi
kook = input("Koogi nimi (sobivad '�okolaadikook', 'ploomikook ja 'Napoleoni kook'): ")
while kook == "�okolaadikook" or kook =="ploomikook" or kook == "Napoleoni kook":
    m��t = float(input("Koogi m��t: "))
    def koogi_hind(kook, m��t):
        if kook == "�okolaadikook":
           hind= m��t ** 2 * pi * 0.06
        elif kook == "ploomikook":
            hind = m��t ** 2 * pi * 0.04
        else:
            hind = m��t * m��t * 0.10
        return(round(hind, 2))
    print(koogi_hind(kook, m��t))
    kook = input("Koogi nimi (sobivad '�okolaadikook', 'ploomikook ja 'Napoleoni kook'): ")
    if kook == "":
        break
else:
    print("Sellist kooki andmebaasist ei leidu.")
        