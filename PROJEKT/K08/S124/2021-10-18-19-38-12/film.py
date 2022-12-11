def loetleFilmid(žanr):
    f = open("filmid.txt", encoding = "UTF-8")
    filmid = []
    for rida in f:
        rida = rida.strip()
        if žanr == rida.split(" - ")[1]:
            film = rida.split(" - ")[0] 
            filmid += [film]
    f.close()
    return filmid
def lisaFilm(nimi,žanr):
    f = open("filmid.txt", "a", encoding = "UTF-8")
    uus_film = ("\n" + nimi + " - " + žanr)
    f.write("{}".format(uus_film))
    f.close()
def kustutaFilm(film):
    f = open("filmid.txt", "r", encoding = "UTF-8")
    read = f.readlines()
    fail = open("filmid.txt", "w", encoding = "UTF-8")
    for rida in read:
        if film != rida.split(" - ")[0]:
            fail.write(rida)
    f.close()
    fail.close()
    