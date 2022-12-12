def loetleFilmid(žanr):
    f = open("filmid.txt", encoding="UTF-8")
    loetelu = []
    for rida in f:
        otsitav = rida.split(" - ")
        if žanr in rida:
            loetelu.append(otsitav[0])
    f.close()
    return loetelu
def lisaFilm(nimi, žanr):
    with open ("filmid.txt", "a") as nimekiri:
        nimekiri.write("\n" + nimi + " - " + žanr)
    nimekiri.close()
def kustutaFilm(filmi_nimi):
    with open ("filmid.txt", "r") as nimekiri:
        read = nimekiri.readlines()
        with open ("filmid.txt", "w") as nimekiri:
            for rida in read:
                otsitav = rida.split(" - ")
                if filmi_nimi in rida:
                    continue
                else:
                    nimekiri.write(rida)
        