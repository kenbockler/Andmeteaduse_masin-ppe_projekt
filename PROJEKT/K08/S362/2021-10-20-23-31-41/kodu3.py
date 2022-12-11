from film import*
def töötleKäsk(käsu_tähis, järjend):
    käsu_tähis=järjend[0].upper()
    f=open("filmid.txt", encoding="UTF-8")
    filmid_zanrid=[]
    for rida in f:
        filmid_zanrid=filmid_zanrid+[rida.strip().split(" - ")]
    zanrid=[]
    for el in filmid_zanrid:
        if el!=[""]:
            if el[1] not in zanrid:
                zanrid=zanrid+[el[1]]
    f.close()
    if käsu_tähis=="K":
        zanr=järjend[1].lower()
        if zanr not in zanrid:
            print("Selle zanriga filme sul veel pole. Kui tahad, lisa.")
            vastus=True
        else:
            käsk=loetleFilmid(zanr)
            uus_list=[]
            for el in käsk:
                uus_list=uus_list+[(el+ "\n")]
            filmid="".join(uus_list)
            print("Võimalikud filmid on:")
            print(filmid)
            vastus=True
    elif käsu_tähis=="L":
        zanr=järjend[1].lower()
        nimi=" ".join(järjend[2:])
        käsk=lisaFilm(nimi, zanr)
        print("Film lisatud!")
        vastus=True
    elif käsu_tähis=="V":
        nimi=" ".join(järjend[1:])
        käsk=kustutaFilm(nimi)
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
        vastus=True
    elif käsu_tähis=="E":
        vastus=False
    return vastus
print("=== FILMIANDMEBAAS ===")
print("Kuva filmid: K <žanr>")
print("Lisa film:   L <žanr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("Lõpeta:      E")
print("===")
while True:
    sisend=input(">")
    järjend=sisend.split(" ")
    käsu_tähis=järjend[0].upper()
    vastus=töötleKäsk(käsu_tähis, järjend)
    if vastus==False:
        break
