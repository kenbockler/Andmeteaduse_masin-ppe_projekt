def loetleFilmid(�anr):
    f = open("filmid.txt")
    filmilist = []
    for rida in f:
        if �anr in rida:
            eemaldan_�anri = rida.strip().replace(�anr, "")
            film = eemaldan_�anri.replace(" - ", "")
            filmilist.append(film)
    return filmilist
    f.close()
def lisaFilm(nimi, �anr):
    f = open("filmid.txt", "a")
    film = nimi + " - " + �anr + "\n"
    f.write("\n"+film)
    f.close()
def kustutaFilm(nimi):
    f = open("filmid.txt", "r")
    read = f.readlines()
    f.close()
    f = open("filmid.txt", "w")
    for rida in read:
        if nimi not in rida:
            f.write(rida)
    f.close()
