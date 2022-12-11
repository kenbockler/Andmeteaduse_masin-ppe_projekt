from film import *
def töötleKäsk(käsk, *args):
  if käsk == "E":
    False
  elif käsk == "K":
      print("Võimalikud filmid on:")
      for film in filmid:
          print(film)
  elif käsk == "L":
        žanr = valikud[0]
        del valikud[0]
        nimi = " ".join(valikud)
        lisaFilm(nimi, žanr)
        print("Film lisatud!")
  elif käsk == "V":
        kustutaFilm(nimi)
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
user_inp = input("=== FILMIANDMEBAAS ===\n"+
              "Kuva filmid: K <žanr>\n"+
              "Lisa film:   L <žanr> <film>\n"+
              "Vaata filmi: V <filmi nimi>\n"+
              "Lõpeta:      E\n"+
              "===\n")
while True:
    käsk = user_inp[0]
    valik = user_inp[2:]
    if käsk == "K":
        filmid = loetleFilmid(valik)
        if len(filmid) == 0:
              print("Pole sellise žanriga filmi. Vali uuesti.\n")
              user_inp = input("=== FILMIANDMEBAAS ===\n"+
              "Kuva filmid: K <žanr>\n"+
              "Lisa film:   L <žanr> <film>\n"+
              "Vaata filmi: V <filmi nimi>\n"+
              "Lõpeta:      E\n"+
              "===\n")
        else:
            töötleKäsk(käsk, valik)
            break
    elif käsk == "V":
        nimi = valik
        töötleKäsk(käsk, nimi)
        break
    else:
        valikud = valik.split()
        töötleKäsk(käsk, valikud)
        break
