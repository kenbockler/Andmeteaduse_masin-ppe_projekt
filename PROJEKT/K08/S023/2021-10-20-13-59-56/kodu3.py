import film
print("""=== FILMIANDMEBAAS ===
Kuva filmid: K <�anr>
Lisa film:   L <�anr> <film>
Vaata filmi: V <filmi nimi>
L�peta:      E
===""")
sisend = input("Sisestage k�sk: ")
while True:
    if sisend == "K" or sisend == "k":
        zanr = input("Sisestage zanr: ")
        kodu2.loetleFilmid(zanr)
    elif sisend == "L" or sisend == "l":
        nimi = input("Sisesta filmi nimi, mida soovid lisada: ")
        zanr = input("Sisetage filmi zanr, mida siivte lisada: ")
        kodu2.lisaFilm(nimi, zanr)
        print("Film lisatud!")
    elif sisend == "V" or sisend == "v":
        nimi = input("Sisesta filmi nimi, mida soovid vaadata: ")
        kodu2.kustutaFilm(nimi)
        print("""Film nimekirjast kustutatud!
Head vaatamist!""")
    elif sisend == "E" or sisend == "e":
        break