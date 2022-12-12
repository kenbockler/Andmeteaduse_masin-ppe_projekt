import film
def töötleKäsk(käsk, *args):
    if len(args[0]) == 0 and not käsk == "E":
        print("See käsklus nõuab argumente")
        return True
    if käsk == "K":
        filmid = film.loetleFilmid(" ".join(args[0]))
        print("Võimalikud filmid on:")
        for f in filmid:
            print(f)
        return True
    elif käsk == "L":
        film.lisaFilm(" ".join(args[0][1:]), args[0][0])
        print("Film listatud!")
        return True
    elif käsk == "V":
        film.kustutaFilm(" ".join(args[0][:]))
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
        return True
    elif käsk == "E":
        return False
    else:
        print("Sobimatu käsklus!")
        return True
print("""
=== FILMIANDMEBAAS ===
Kuva filmid: K <žanr>
Lisa film:   L <žanr> <film>
Vaata filmi: V <filmi nimi>
Lõpeta:      E
===
""")
jätka = True
while jätka:
    sisend = input("@ ").split()
    jätka = töötleKäsk(sisend[0].upper(), sisend[1:])
