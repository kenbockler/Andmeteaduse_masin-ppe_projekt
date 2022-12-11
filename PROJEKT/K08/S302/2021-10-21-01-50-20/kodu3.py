from film import *
def töötleKäsk(seis, sisu):
    if seis == "K":
        print(loetleFilmid(str(sisu[0])))
        return True
    elif seis == "L":
        print(sisu)
        lisaFilm(sisu[1], sisu[0])
        print("Film lisatud!")
        return True
    elif seis == "V":
        print(sisu[0])
        kustutaFilm(str(sisu[0]))
        print("Film nimekirjast kustutatud!\nHead vaatamist!")
        return True
    elif seis == "E":
        exit()
    else:
        print("Tundmatu käsk, proovi uuesti!")
        return True
print("=== FILMIANDMEBAAS ===")
print("Kuva filmid:  K <žanr>")
print("Lisa film:    L <žanr> <film>")
print("Vaata filmi:  V <filmi nimi>")
print("Lõpeta:       E ")
print("===")
while True:
    inp = input("> ")
    uus = inp.split(" ")
    käsk = uus[0]
    k = 0
    lol = []
    lol = uus[1:]
    if käsk == "V":
        lol = []
        lol.append(inp[2:])
    if käsk == "L":
        lol = []
        uus2 = []
        uus2 = inp[2:]
        appi = "".join(uus2).split(" ")
        idk = appi[1:]
        aaa = " ".join(idk)
        lol.append(appi[0])
        lol.append(aaa)
        print(aaa)
    töötleKäsk(käsk, lol)