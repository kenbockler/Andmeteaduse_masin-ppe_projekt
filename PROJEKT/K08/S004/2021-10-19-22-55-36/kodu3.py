from film import loetleFilmid
from film import kustutaFilm
from film import lisaFilm
def t��tleK�sk(t�his,j�rjend):
    if t�his == "K":
        if len(loetleFilmid(j�rjend)) > 0:
            for x in loetleFilmid(j�rjend):
                print(x)
        else:
            print("Selliseid filme pole")
        return True
    if t�his == "L":
        a=j�rjend.split(" ",1)
        print(a)
        lisaFilm(a[1],a[0])
        return True
    if t�his == "V":
        kustutaFilm(j�rjend)
        return True
    if t�his == "E":
        return False
while True:
    sisend=str(input(""))
    u=sisend.split(" ",1)
    if u[0]=="E":
        u.append("")
    print(u)
    if t��tleK�sk(u[0],u[1]) == False:
        break