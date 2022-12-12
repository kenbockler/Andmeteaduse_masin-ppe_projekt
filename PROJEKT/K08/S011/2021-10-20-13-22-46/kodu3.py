import film
print(" ===FILMI ANDMEBAAS=== \n Kuva filmid: K <žanr> \n Lisa film:   L <žanr> <film> \n Vaata filmi: V <filmi nimi> \n Lõpeta:      E \n ===")
def töötleKäsk(täht, järjend):
    tähis = täht.upper()
    if tähis == "K" :
        žanr = järjend[0]
        print("Võimalikud filmid on: ", loetleFilmid({žanr}))
    elif tähis == "L" :
        nimi = järjend[1:]
        žanr = järjend[0]
        lisaFilm({nimi},{žanr})
        print ("Film on edukalt lisatud!")
    elif tähis == "V" :
        nimi =  järjend[0:]
        kustutaFilm({nimi})
        print("Film nimekirjast kustutatud! \n Head vaatamist!")
while True:
    käsk = ((input("Sisesta käsk: ")).split(" "))
    täht = str(käsk[0])
    if täht == "E":
        break
    järjend = str(käsk[1:])
    töötleKäsk(täht, järjend)