def loetleFilmid(�anr):
    otsitav = �anr
    with open("filmid.txt") as f:
        filmid = f.readlines()
    otsitavad = []
    for film in filmid:
        if otsitav in film:
            filmi_nimi = film.strip(" - {otsitav}")
            otsitavad = otsitavad + filmi_nimi
    return (otsitavad)
def lisaFilm(nimi,�anr):
    f = open('filmid.txt', 'a+')
    f.write("{nimi} - {�anr}","\n")
    f.close
def kustutaFilm(nimi):
    kustutada = nimi
    with open('filmid.txt','r') as f:
        filmid_�hekaupa = f.readlines()
    with open('filmid.txt','w') as f:
        for film in filmid_�hekaupa:
            if film.strip("\n") != (kustutada):
                f.write(film)
    