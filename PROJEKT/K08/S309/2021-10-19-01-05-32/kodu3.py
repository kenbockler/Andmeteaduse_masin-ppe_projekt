import film
def töötleKäsk(cmd, args):
        if cmd == "K":
            print("Võimalikud filmid on:")
            for i in film.loetleFilmid(args[0]): print(i)
            print("\n")
        elif cmd == "L":
            film.lisaFilm(str(" ".join(args[1:len(args)])), args[0])
            print("Film lisatud!")
            print("\n")
        elif cmd == "V":
            film.kustutaFilm(str(" ".join(args[0:len(args)])))
            print("Film nimekirjast kustutatud!\nHead vaatamist!")
            print("\n")
        elif cmd == "E":
            print(">>>")
try:
    loopcondition = True
    print("=== FILMIANDMEBAAS ===")
    print("Kuva filmid: K <žanr>")
    print("Lisa film:   L <žanr> <film>")
    print("Vaata filmi: V <filmi nimi>")
    print("Lõpeta:      E")
    print("===")
    while loopcondition:
        userinput = str(input()).split(" ")
        töötleKäsk(userinput[0], userinput[1:len(userinput)])
        if userinput[0] == "E":
            loopcondition = False
except Exception as e:
    print(e)