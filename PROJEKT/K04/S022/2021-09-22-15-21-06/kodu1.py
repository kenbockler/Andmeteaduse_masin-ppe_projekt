from math import pi
z=0
t=0
while t==0:
    a=input("�tle koogi nimi. ")
    if len(a) == 0:
        break
    b=float(input("�tle oma koogi raadius voi k�ljemoot. "))
    def koogi_hind(a, b):
        if a == "�okolaadikook":
            S = pi*b**2
            hind = S * 0.06
            hind = round(hind, 2)
            return hind
        elif a == "ploomikook":
            S = pi *b**2
            hind = S * 0.04
            hind = round(hind, 2)
            return hind
        elif a == "Napoleoni kook":
            S = b**2
            hind = S * 0.1
            hind = round(hind, 2)
            return hind
        else:
            raise Exception("Sellist kooki andmebaasist ei leitud.")
            return 
    print(koogi_hind(a, b))