def loetleFilmid(žanr):
    fail = open("filmid.txt", "r", encoding="UTF-8")
    järjend = []
    uus_järjend = []
    for rida in fail:
        järjend = rida.split(" - ")
        nimi = järjend[0].strip()
        žanr_1 = järjend[1].strip("\n")
        uus_järjend.append(nimi)
        uus_järjend.append(žanr_1)
        žanride_indeksid = []
        filmide_nimed = []
    for i in range(len(uus_järjend)):
        if uus_järjend[i] == žanr:
            žanride_indeksid.append(i)
    for j in range(len(žanride_indeksid)):
        filmide_nimed.append(uus_järjend[žanride_indeksid[j] - 1])
    fail.close()
    return filmide_nimed
def lisaFilm(nimi, žanr):
    fail = open("filmid.txt", "a", encoding="UTF-8")
    fail.write("\n")
    fail.write(" ")
    fail.write(nimi)
    fail.write(" - ")
    fail.write(žanr)
    fail.close()
def kustutaFilm(nimi):
    fail = open("filmid.txt", "r", encoding="UTF-8")
    for rida in fail:
        read = fail.readlines()
        if nimi in read:
            kustutamiseks = rida
    fail.close()
    fail = open("filmid.txt", "w", encoding="UTF-8")
    for rida in read:
        if rida.strip("\n") != kustutamiseks:
            fail.write(rida)
    fail.close()
