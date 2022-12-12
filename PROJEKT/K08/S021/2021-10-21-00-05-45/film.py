def loetleFilmid(žanr):
    f = open("filmid.txt","r", encoding = "UTF-8")
    järjend = []
    for film in f:
        filmijärjend = film.strip().split(" - ")
        if žanr == filmijärjend[-1]:
            järjend = järjend + [filmijärjend[0]]
            continue
        else:
            continue
    f.close()
    return järjend
def lisaFilm(nimi, žanr):
    f = open("filmid.txt","a", encoding = "UTF-8")
    f.write("\n" + nimi + " - " + žanr)
    f.close()
def kustutaFilm(nimi):
    uusjärjend = []
    f = open("filmid.txt","r", encoding = "UTF-8")
    for film in f:
        järjend = film.strip().split(" - ")
        if järjend[0] == nimi:
            continue
        else:
            uusjärjend = uusjärjend + [film]
            continue
    f.close()
    i = 0
    f = open("filmid.txt","w", encoding = "UTF-8")
    while i < len(uusjärjend):
        kirjutatav = uusjärjend[i]
        f.write(kirjutatav)
        i += 1
    f.close()
