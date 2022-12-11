def loetleFilmid(žanr):
    nimed = []
    f = open("filmid.txt", encoding = "UTF-8")
    for rida in f:
        rea_osad = rida.split(" - ")
        x = len(rea_osad)
        if rea_osad[x-1].strip("\n") == žanr:
            nimed.append(rea_osad[0].strip(" "))
    f.close
    return(nimed)
def lisaFilm(nimi, žanr):
    f = open("filmid.txt", "a", encoding = "UTF-8")
    f.write("\n"+nimi+" - "+žanr)
    f.close
def kustutaFilm(nimi):
    f = open("filmid.txt", "r", encoding = "UTF-8")
    read = f.readlines()
    f = open("filmid.txt", "w", encoding = "UTF-8")
    for rida in read:
        rea_osad = rida.split(" - ")
        x = len(rea_osad)
        if rea_osad[x-2].strip("\n") != nimi:
            f.write(rida)
kustutaFilm("Spider-Man")
            