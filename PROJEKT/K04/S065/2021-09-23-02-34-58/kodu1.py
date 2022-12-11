a = input("Sisestage koogi nimi: ")
b = float(input("Sisestage koogi mõõt (cm): "))
def koogi_hind(nimi, mõõt):
    if nimi.lower() != "Šokolaadikook" and nimi.lower() != "Ploomikook" and nimi.lower() != "Napoleoni kook":
        return ("Sellist kooki andmebaasis ei leitud.")
    elif nimi.lower() == "Šokolaadikook":
        hind = (math.pi*mõõt**2)*0.06
        return (round(hind,2))
    elif nimi.lower() =="Ploomikook":
        hind = (math.pi*mõõt**2)*0.04
        return (round(hind,2))
    elif nimi.lower() == "Napoleoni kook":
        hind = mõõt**2*0.10
        return (round(hind,2))
print(koogi_hind(a,b))