import film
def t��tleK�sk(t�his, j�rjend):
    if t�his == "E":
        return False
    elif t�his == "K":
        �anr = j�rjend[0]
        a = film.loetleFilmid(�anr)
        print("V�imalikud filmid on:\n", a)
        return True
    elif t�his == "L":
        �anr = j�rjend[0]
        nimi = " ".join(j�rjend[1:])
        film.lisaFilm(�anr, nimi)
        print("Film lisatud!")
        return True
    elif t�his == "V":
        nimi = " ".join(j�rjend[0:])
        film.kustutaFilm(nimi)
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
        return True
while True:        
    sisestus = input("Sisesta info: ").split()
    t�his = sisestus[0]
    j�rjend = sisestus[1:]
    if t��tleK�sk(t�his, j�rjend):
        continue
    else:
        break
    