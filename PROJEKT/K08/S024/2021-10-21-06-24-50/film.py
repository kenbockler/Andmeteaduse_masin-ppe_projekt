def loetleFilmid(�anr):
    fail = open("filmid.txt", "r", encoding="UTF-8")
    j�rjend = []
    uus_j�rjend = []
    for rida in fail:
        j�rjend = rida.split(" - ")
        nimi = j�rjend[0].strip()
        �anr_1 = j�rjend[1].strip("\n")
        uus_j�rjend.append(nimi)
        uus_j�rjend.append(�anr_1)
        �anride_indeksid = []
        filmide_nimed = []
    for i in range(len(uus_j�rjend)):
        if uus_j�rjend[i] == �anr:
            �anride_indeksid.append(i)
    for j in range(len(�anride_indeksid)):
        filmide_nimed.append(uus_j�rjend[�anride_indeksid[j] - 1])
    fail.close()
    return filmide_nimed
def lisaFilm(nimi, �anr):
    fail = open("filmid.txt", "a", encoding="UTF-8")
    fail.write("\n")
    fail.write(" ")
    fail.write(nimi)
    fail.write(" - ")
    fail.write(�anr)
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
