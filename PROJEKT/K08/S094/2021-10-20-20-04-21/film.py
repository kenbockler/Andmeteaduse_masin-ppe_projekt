def loetleFilmid(zanr):
    sobivad_filmid = []
    with open("filmid.txt", encoding="utf-8") as f:
        while True:
            loendur = f.readline().strip()
            if loendur == "":
                break
            if zanr in loendur:
                sobivad_filmid += [loendur]
    return sobivad_filmid
def lisaFilm(nimi,zanr):
    with open("filmid.txt", "a",encoding="utf-8") as f:        
        f.write(nimi, "-", zanr)
def kustutaFilm(nimi):
    with open("filmid.txt", "r",encoding="utf-8") as f:
        sisu = f.readlines()
        with open("filmid.txt", "w",encoding="utf-8") as f:
            for rida in sisu:
                if rida.strip("\n") != nimi:
                    f.write(rida)                                 
