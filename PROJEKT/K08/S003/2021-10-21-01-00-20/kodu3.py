from film import *
def t��tleK�sk(t�his,j�rjend=[]):
    if t�his == "K":
        filmid = loetleFilmid(j�rjend[0])
        print("v�imalikud filmid on!")
        for el in filmid:
            print(el)
        return True
    elif t�his == "L":
        lisaFilm(j�rjend[1],j�rjend[0])
        print("Film lisatud!")
        return True
    elif t�his == "V":
        kustutaFilm(j�rjend[0])
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
        return True
    elif t�his == "E":
        return False
    else:
        print("Vale k�sk!")
t��tab = True
while t��tab:
    sisend = input()
    sisendi_osad = sisend.split(" ",1)
    t�his = sisendi_osad[0]
    if len(sisendi_osad) > 1:
        sisendi_osad = sisendi_osad[1].split(" ",1)
    t��tab = t��tleK�sk(t�his,sisendi_osad)
    