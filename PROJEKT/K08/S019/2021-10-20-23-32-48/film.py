f = open("filmid.txt", encoding ="UTF-8")
a = [ ]
def loetleFilmid(zanr):
    for rida in f:
        if rida == " ":
            break
        j�r = rida.split(" - ")
        if j�r[1] == zanr:
            a.append(j�r[0])
    return a
def lisaFilm(nimi, zanr):
    rida = nimi, "-", zanr
    f.write(rida)
def kustutaFilm(nimi):
    