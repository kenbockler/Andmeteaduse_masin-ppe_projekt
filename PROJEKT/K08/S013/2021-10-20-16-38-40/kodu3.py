import film
def t��tleK�sk(t�his, j�rjend):
    if t�his == "K":
        sann = j�rjend[0]
        print(("V�imalikud filmid on: ") + str(film.loetleFilmid(sann)))
        return True
    elif t�his == "L":
        sann = j�rjend[0]
        film.lisaFilm(" ".join(z), sann)
        print("Film lisatud")
        return True
    elif t�his == "V":
        kustutamine = j�rjend[1: len(j�rjend)]
        film.kustutaFilm(" ".join(kustutamine))
        print("Film nimekirjast kustutatud!\n Head vaatamist!")
        return True
    elif t�his == "E":
        return False
print("=== FILMIANDMEBAAS ===\n Kuva filmid: K <�anr>\n Lisa film:   L <�anr> <film>\n Vaata filmi: V <filmi nimi>\n L�peta:      E\n ===")
x = input().split()
j�rjend = x
y = j�rjend[0]
z = j�rjend[1: len(j�rjend)]
while t��tleK�sk(y, z) == True:
    x = input().split()
    j�rjend = x
    y = j�rjend[0]
    z = j�rjend[1: len(j�rjend)]
    