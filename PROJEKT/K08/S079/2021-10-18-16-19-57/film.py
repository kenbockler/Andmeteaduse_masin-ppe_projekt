def loetleFilmid(žanr):
    f = open("filmid.txt", "r")
    nimed = []
    žanrid = []
    for rida in f:
        r = rida.strip().split(" - ")
        nimed.append(r[0])
        žanrid.append(r[1])
    f.close()
    a = []
    for i in range(len(žanrid)):
        if žanrid[i] == žanr:
            a.append(nimed[i])
    return a
def lisaFilm(nimi, žanr):
    lisatav_film = "\n" + nimi + " - " + žanr
    f = open("filmid.txt", "a")
    f.write(lisatav_film)
    f.close()
def kustutaFilm(nimi):
    f = open("filmid.txt", "r")
    uus = []
    for rida in f:
        if nimi not in rida:
            uus.append(rida)
    f.close()
    f = open("filmid.txt", "w")
    for rida in uus:
        f.write(rida)
    f.close()