import math
def koogi_hind(koogi_nimi, m��t):
    if koogi_nimi== ("Napoleoni kook"):
       hind = round(0.10*m��t*m��t,2)
       return hind
    if koogi_nimi==("�okolaadikook"):
        hind = round(0.06*m��t**2*(math.pi),2)
        return hind
    if koogi_nimi ==("ploomikook"):
        hind=round(0.04*m��t**2*(math.pi),2)
        return hind
    return Exception("Sellist kooki andmebaasist ei leitud.")
while True:
    nimi=str(input('Sisestage kooginimi: '))
    if nimi == (""):
        break
    m��t=float(input("Sisestage koogi m��t: "))
    print(koogi_hind(nimi, m��t))
