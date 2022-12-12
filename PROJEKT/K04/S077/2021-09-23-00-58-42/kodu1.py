from math import pi
def koogi_hind(a,b):
    if a=="šokolaadikook":
        return round(pi*b**2*0.06,2)
    elif a=="ploomikook":
        return round(pi*b**2*0.04,2)
    elif a=="Napoleoni kook":
        return round(b**2*0.10,2)
    else:
        raise ValueError("Sellist kooki andmebaasis ei leitud.")
nimi=input("Sisesta koogi nimi: ")
while nimi!="":
    mõõt=float(input("Sisesta koogi mõõt sentimeetrites: "))
    print("Koogi hind on",str(koogi_hind(nimi,mõõt)),"eurot.","\n")
    nimi=input("Sisesta koogi nimi: ")
