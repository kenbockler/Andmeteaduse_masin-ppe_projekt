import film
def t��tleK�sk(t�his, j�rjend):
    if t�his == "K":
        rida=film.loetleFilmid(j�rjend[0])
        print(f"V�imalikud filmid on:\n {rida}")
        return True
    elif t�his == "L":
        zanr=j�rjend[0]
        pealkiri=j�rjend[1:]
        pealkiri=" ".join(pealkiri)
        film.lisaFilm(pealkiri, zanr)
        return True
    elif t�his =="V":
        film.kustutaFilm(" ".join(j�rjend))
        print("Film nimekirjast kustutaud! \n Head vaatamist")
        return True
    else:
        return False
x=True
while x==True:
    sisend=input()
    sisend=sisend.split(" ")
    x=t��tleK�sk(sisend[0],sisend[1:])
