from math import pi
def koogi_hind(ruut_cm_hind, pindala):
    return ruut_cm_hind * pindala
m��t = float(input("Sisesta m��t sentimeetrites:"))
nimi = input("Sisesta koogi nimi:")
if nimi == "�okolaadikook":
    ruut_cm_hind = 0.06
    pindala = ((m��t**2) * pi)
    print("Sellise �okolaadikoogi hind on", round(koogi_hind(ruut_cm_hind, pindala), 3), "eurot.")
elif nimi == "ploomikook":
    ruut_cm_hind = 0.04 
    pindala = ((m��t**2) * pi)
    print("Sellise ploomikoogi hind on", round(koogi_hind(ruut_cm_hind, pindala), 3), "eurot.")
elif nimi == "Napoleoni kook":
    ruut_cm_hind = 0.10
    pindala = (m��t**2)
    print("Sellise Napoleoni koogi hind on", round(koogi_hind(ruut_cm_hind, pindala), 3), "eurot.")
else:
    print("Sellist kooki andmebaasist ei leitud.")
    