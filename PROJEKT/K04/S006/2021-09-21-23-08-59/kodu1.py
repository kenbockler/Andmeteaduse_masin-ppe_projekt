from math import*
while True:
    nimi = input("Valikus on �okolaadikook, ploomikook ja Napoleoni kook. Milline kook on meelep�raseim? ")
    if nimi == "":
        break
    m��t = float(input("Sisesta koogit�ki suurus sentimeetrites: "))
    def koogi_hind(nimi, m��t):
        if nimi == "�okolaadikook":
            return(round(m��t*m��t*0.06*pi, 2))
        elif nimi == "ploomikook":
            return(round(m��t*m��t*0.04*pi, 2))
        elif nimi == "Napoleoni kook":
            return(round(m��t*m��t*0.10, 2))
        else:
            raise Exception("Sellist kooki andmebaasist ei leitud.")
    print("Koogit�ki hind on ", koogi_hind(nimi, m��t), " eurot.")
