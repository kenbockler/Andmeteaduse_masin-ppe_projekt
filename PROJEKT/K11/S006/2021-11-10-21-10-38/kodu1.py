with open("lapsed.txt") as flapsed, open("nimed.txt") as fnimed:
    def seosta_lapsed_ja_vanemad(flapsed, fnimed):
        uus = {}
        uus2 = []
        uus3 = {}
        indeks = 0
        for rida in fnimed:
            j�rjend = rida.split(" ")
            kood = j�rjend[0]
            nimi = j�rjend[1] + " " + j�rjend[2]
            uus[kood] = nimi.strip("\n")
        for rida in flapsed:
            t�hi = {}
            j�rjend2 = rida.strip().split()
            if j�rjend2[1] in uus:
                t�hi[uus[j�rjend2[1]]] = set([uus[j�rjend2[0]]])
                uus2.append(uus[j�rjend2[1]])
                uus2.append(uus[j�rjend2[0]])
            else:
                continue
        for element in uus2:
            if indeks % 2 != 0:
                indeks += 1
            elif uus2[indeks] not in uus3:
                uus3[element] = set([uus2[indeks + 1]])
                indeks += 1
            else:
                uus3[element] = set([" ".join(uus3[element]) + ", "+ uus2[indeks + 1]])
                indeks += 1
        return uus3
    tagastus = seosta_lapsed_ja_vanemad(flapsed, fnimed)
    for laps in tagastus:
        print(laps + ": " + " ".join(tagastus[laps]))
