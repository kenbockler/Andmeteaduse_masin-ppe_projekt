import film
def töötleKäsk(tähis, järjend):
    if tähis == "E":
        return False
    elif tähis == "K":
        žanr = järjend[0]
        a = film.loetleFilmid(žanr)
        print("Võimalikud filmid on:\n", a)
        return True
    elif tähis == "L":
        žanr = järjend[0]
        nimi = " ".join(järjend[1:])
        film.lisaFilm(žanr, nimi)
        print("Film lisatud!")
        return True
    elif tähis == "V":
        nimi = " ".join(järjend[0:])
        film.kustutaFilm(nimi)
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
        return True
while True:        
    sisestus = input("Sisesta info: ").split()
    tähis = sisestus[0]
    järjend = sisestus[1:]
    if töötleKäsk(tähis, järjend):
        continue
    else:
        break
    