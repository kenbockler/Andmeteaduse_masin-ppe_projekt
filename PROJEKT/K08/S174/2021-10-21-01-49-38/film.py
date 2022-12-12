def loetleFilmid(žanr):
    fail = open("filmid.txt")
    filmid = fail.readlines()
    tulemusjärjend = []
    for rida in filmid:
        if žanr in rida:
            filmilist = rida.split(" - ")
            filminimi = filmilist[0]
            tulemusjärjend.insert(0, filminimi)
    fail.close()
    return tulemusjärjend
def lisaFilm(nimi, žanr):
    fail = open("filmid.txt", "a")
    rida = "\n" + nimi + " - " + žanr
    fail.write(rida)
    fail.close()
def kustutaFilm(nimi):
    fail = open("filmid.txt", "r")
    read = fail.readlines()
    fail.close()
    fail = open("filmid.txt", "w")
    for rida in read:
        if nimi != rida.split(" - ")[0]: 
            fail.write(rida)
    fail.close()
