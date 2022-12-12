import film
def töötleKäsk(käsu_tähis, järjend_käsu_argumentidega):
    if käsu_tähis == "K":
        žanr = järjend_käsu_argumentidega[0]
        print("Võimalikud filmid on:")
        järjend = film.loetleFilmid(žanr)
        i = 0
        for el in järjend:
            print(järjend[i])
            i += 1
        tagastus = True
    elif käsu_tähis == "L":
        nimi = järjend_käsu_argumentidega[1]
        žanr = järjend_käsu_argumentidega[0]
        film.lisaFilm(nimi, žanr)
        print("Film lisatud!")
        tagastus = True
    elif käsu_tähis == "V":
        nimi = järjend_käsu_argumentidega[0]
        film.kustutaFilm(nimi)
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
        tagastus = True
    elif käsu_tähis == "E":
        tagastus = False
    return tagastus
print("=== FILMIANDMEBAAS ===")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta:      E")
print("===")
while True:
    käsk = input("> ")
    käsk = käsk.split(" ")
    käsu_tähis = käsk[0]
    if käsu_tähis == "L":
        žanr = käsk[1]
        nimi = " ".join(käsk[2:])
        järjend_käsu_argumentidega = [žanr, nimi]
    elif käsu_tähis == "E":
       järjend_käsu_argumentidega = [""]
    else:
        muu = " ".join(käsk[1:])
        järjend_käsu_argumentidega = [muu]
    vastus = töötleKäsk(käsu_tähis, järjend_käsu_argumentidega)
    if vastus == False:
        break
