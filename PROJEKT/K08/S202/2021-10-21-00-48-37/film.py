f = open("filmid.txt", encoding="utf-8")
a = open("filmid.txt", "a", encoding="utf-8")
def loetleFilmid(žanr):
    final = []
    while True:
        liner = f.readline()
        if len(liner) > 0:
            if žanr in liner:
                round2 = liner.split(" - ")
                filmn = round2[0]
                final += [str(filmn)]
        else:
            break
    f.close()
    return(final)
def lisaFilm(filminimi, filmitüüp):
    ffinal = filminimi + " - " + filmitüüp
    a.write("\n" + ffinal)
    a.close()
def kustutaFilm(filnim):
    r = open("filmid.txt", "r", encoding="utf-8")
    linerr = r.readlines()
    r.close()
    w = open("filmid.txt", "w", encoding="utf-8")
    for linerrr in linerr:
        if filnim not in linerrr:
            w.write(linerrr)
    w.close()
f.close()
