from film import loetleFilmid
from film import lisaFilm
from film import kustutaFilm
def t��tleK�sk(tahis, jarjend):
    if tahis == "K":
        if loetleFilmid(jarjend) == "":
            print("Valitud �anrist pole �htegi filmi, valige uuesti")
            return True
        for film in loetleFilmid(jarjend):
            print(film)
        return True
    if tahis == "L":
        list1 = jarjend.split(" ")
        a = 1
        nimi = ""
        for obj in list1:
            if a == 1:
                tuup = obj
                a = 2
                continue
            if a == 2:
                nimi = nimi + " " + obj
        lisaFilm(nimi, tuup)
        print("Film lisatud! ")
        return True
    if tahis == "V":
        kustutaFilm(jarjend)
        print("Film kustutatud! Head Vaatamist!")
        return True
    if tahis == "E":
        return False
print("=== FILMIANDMEBAAS ===")
print("Kuva filmid: K <�anr>")
print("Lisa film:   L <�anr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("L�peta:      E")
print("===")
while True:
    sisend = input("")
    if sisend == "E":
        break
    film1 = sisend.split(" ")
    a = 1
    jarjend = ""
    for osa in film1:  
        if a == 1:
            osa = osa.strip()
            tahis = osa
            a = 2
            continue
        if a == 2:
            osa = osa.strip()
            jarjend = jarjend + osa + " "
    jarjend = jarjend.strip()
    t��tleK�sk(tahis, jarjend)
"""    if len(film1) == 1:
        film1[0] = film1[0].strip()
        tahis = film1[0]
        jarjend = ""
    if len(film1) == 2:
        film1[1] = film1[1].strip()
        film1[0] = film1[0].strip()
        tahis = film1[0]
        jarjend = film1[1]
    if len(film1) == 3:
        film1[1] = film1[1].strip()
        film1[0] = film1[0].strip()
        film1[2] = film1[2].strip()
        film1[1] = film1[1] + " " + film1[2]
        tahis = film1[0]
        jarjend = film1[1]
    if len(film1) == 4:
        film1[1] = film1[1].strip()
        film1[0] = film1[0].strip()
        film1[2] = film1[2].strip()
        film1[3] = film1[3].strip()
        film1[1] = film1[1] + " " + film1[2] + " " + film1[3]
        tahis = film1[0]
        jarjend = film1[1]
    t��tleK�sk(tahis, jarjend)"""
"""     
    for osa in film1:  
        if a == 1:
            osa = osa.strip()
            tahis = osa
            a = 2
            continue
        if a == 2:
            osa = osa.strip()
            jarjend = jarjend + " " + osa
    t��tleK�sk(tahis, jarjend)"""
"""
for obj in list1:
            if a == 1:
                tuup = obj
                a = 2
                continue
            if a == 2:
                nimi = nimi + " " + obj
                """