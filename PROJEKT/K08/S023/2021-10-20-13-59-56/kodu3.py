import film
print("""=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===""")
sisend = input("Sisestage käsk: ")
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