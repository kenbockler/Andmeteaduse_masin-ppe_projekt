def loetleFilmid(�anr):
    f = open("filmid.txt", encoding="UTF-8")
    loetelu = []
    for rida in f:
        otsitav = rida.split(" - ")
        if �anr in rida:
            loetelu.append(otsitav[0])
    f.close()
    return loetelu
def lisaFilm(nimi, �anr):
    with open ("filmid.txt", "a") as nimekiri:
        nimekiri.write("\n" + nimi + " - " + �anr)
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
        