def loetleFilmid(zanr):
    with open("filmid.txt") as f:
        filmid = []
        faili_read = f.readlines()
        for f in faili_read:
            filmi_info =  f.split(" - ")
            if filmi_info[1].strip() == str(zanr):
                filmid += filmi_info[0]
            else:
                continue
            return(filmid)
def lisaFilm(filmi_nimi, zanr):
    with open("filmid.txt", "a") as f:
        f.write(str(filmi_nimi) + " - " + str(zanr))
def kustutaFilm(filmi_nimi):
    with open("filmid.txt", "r") as f:
        faili_read = f.readlines()
    with open("filmid.txt", "w") as f:
        for rida in faili_read:
            filmi_info = rida.split(" - ")
            if not filmi_info[0] == str(filmi_nimi):
                f.write(rida)
