def loetleFilmid(�anr):
    f = open("filmid.txt","r", encoding = "UTF-8")
    j�rjend = []
    for film in f:
        filmij�rjend = film.strip().split(" - ")
        if �anr == filmij�rjend[-1]:
            j�rjend = j�rjend + [filmij�rjend[0]]
            continue
        else:
            continue
    f.close()
    return j�rjend
def lisaFilm(nimi, �anr):
    f = open("filmid.txt","a", encoding = "UTF-8")
    f.write("\n" + nimi + " - " + �anr)
    f.close()
def kustutaFilm(nimi):
    uusj�rjend = []
    f = open("filmid.txt","r", encoding = "UTF-8")
    for film in f:
        j�rjend = film.strip().split(" - ")
        if j�rjend[0] == nimi:
            continue
        else:
            uusj�rjend = uusj�rjend + [film]
            continue
    f.close()
    i = 0
    f = open("filmid.txt","w", encoding = "UTF-8")
    while i < len(uusj�rjend):
        kirjutatav = uusj�rjend[i]
        f.write(kirjutatav)
        i += 1
    f.close()
