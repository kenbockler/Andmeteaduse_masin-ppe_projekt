from math import pi
def koogi_hind(n, s):
    if n == "�okolaadikook":
        S = pi*s**2
        return(round(S*0.06, 2))
    elif n == "ploomikook":
        S = pi*s**2
        return(round(S*0.04, 2))
    elif n == "Napoleoni kook":
        S = s**2
        return(round(S*0.10, 2))
    else:
        n = int(n)
        return("Sellist kooki andmebaasist ei leitud")
while True:
    nimi = str(input("Sisesta koogi nimi: "))
    if nimi == "":
        break
    m��t = float(input("Sisesta koogi m��t: "))
    print(koogi_hind(nimi, m��t))