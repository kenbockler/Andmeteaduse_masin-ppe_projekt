import film
print(" ===FILMI ANDMEBAAS=== \n Kuva filmid: K <�anr> \n Lisa film:   L <�anr> <film> \n Vaata filmi: V <filmi nimi> \n L�peta:      E \n ===")
def t��tleK�sk(t�ht, j�rjend):
    t�his = t�ht.upper()
    if t�his == "K" :
        �anr = j�rjend[0]
        print("V�imalikud filmid on: ", loetleFilmid({�anr}))
    elif t�his == "L" :
        nimi = j�rjend[1:]
        �anr = j�rjend[0]
        lisaFilm({nimi},{�anr})
        print ("Film on edukalt lisatud!")
    elif t�his == "V" :
        nimi =  j�rjend[0:]
        kustutaFilm({nimi})
        print("Film nimekirjast kustutatud! \n Head vaatamist!")
while True:
    k�sk = ((input("Sisesta k�sk: ")).split(" "))
    t�ht = str(k�sk[0])
    if t�ht == "E":
        break
    j�rjend = str(k�sk[1:])
    t��tleK�sk(t�ht, j�rjend)