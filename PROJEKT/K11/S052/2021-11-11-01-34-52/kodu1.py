def seosta_lapsed_ja_vanemad(lastefail, nimedefail):
    f = open(lastefail, "r")
    nimekiri = {}
    for rida in f:
        vanem = rida.split(" ",1)[0]
        laps = rida.split(" ",1)[1].strip()
        if rida.split(" ")[0] in nimekiri:
            nimekiri[vanem] = nimekiri[vanem] + " " + (laps)
        else:  
            nimekiri[vanem] = laps
    f.close()
    print(nimekiri)
seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
