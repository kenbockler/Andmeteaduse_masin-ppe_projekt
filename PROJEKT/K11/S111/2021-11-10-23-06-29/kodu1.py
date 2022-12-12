def seosta_lapsed_ja_vanemad(lapsed,nimed):
    nimi={}
    for rida in nimed:
        rida=rida.strip().split()
        nimi[rida[0]]=rida[1]+ (" ") + rida[2]
    lõpp={}
    hulk=set()
    for rida in lapsed:
        hulk.clear()
        rida=rida.strip().split()
        if nimi[rida[1]] not in lõpp:
            lõpp[nimi[rida[1]]]=nimi[rida[0]]
        elif nimi[rida[1]] in lõpp:
            hulk.add(lõpp[nimi[rida[1]]])
            hulk.add(nimi[rida[0]])
            lõpp[nimi[rida[1]]]=hulk
    return(lõpp)
lapsed=open("lapsed.txt")
nimed=open("nimed.txt")
print(seosta_lapsed_ja_vanemad(lapsed,nimed))