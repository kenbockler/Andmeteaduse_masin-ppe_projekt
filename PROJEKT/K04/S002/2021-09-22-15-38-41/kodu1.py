from math import pi
def koogi_hind(nimi,m��t):
    if nimi == "�okolaadikook":
        return round((pi*m��t**2)*0.06,2)
    elif nimi == "ploomikook":
        return round((pi*m��t**2)*0.04,2)
    elif nimi == "Napoleoni kook":
        return round((m��t**2)*0.1,2)
    else: raise Exception("Sellist kooki andmebaasist ei leitud")
n = input("Kook")
m = float(input("M��t"))
while True:
    print(koogi_hind(n,m))
    n = input("Kook")
    if n == "":
        break
    m = float(input("M��t"))