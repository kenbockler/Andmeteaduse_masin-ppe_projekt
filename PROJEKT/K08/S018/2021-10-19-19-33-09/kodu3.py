import film
def t��tleK�sk(k, j):
    if k == "K":
        print(film.loetleFilmid(j[0]))
        return True
    elif k == "L":
        film.lisaFilm(j[1], j[0])
        return True
    elif k == "V":
        film.kustutaFilm(j[1])
        return True
    else:
        return False
while True:
    sisend = str(input("Sisend: "))
    sisend = sisend.split()
    k�sk = sisend[0]
    j�rjend = ["", ""]
    if k�sk == "K":
        j�rjend[0] = sisend[1]
    elif k�sk == "L":
        if len(sisend) > 3:
            i = 2
            nimi = ""
            while i < len(sisend):
                nimi = nimi + sisend[i]
                if i + 1 < len(sisend):
                    nimi += " "
                i += 1
        else:
            nimi = sisend[2]
        j�rjend[0] = sisend[1]
        j�rjend[1] = nimi
    elif k�sk == "V":
        if len(sisend) > 2:
            i = 1
            nimi = ""
            while i < len(sisend):
                nimi = nimi + sisend[i]
                if i + 1 < len(sisend):
                    nimi += " "
                i += 1
            j�rjend[0] = sisend[1]
            j�rjend[1] = nimi
        else:
            nimi = sisend[1]
        j�rjend[1] = nimi
    else:
        break
    t��tleK�sk(k�sk, j�rjend)