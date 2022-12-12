import film
while True:
    sisend = input( "\n" +
                    "Kuva filmid: K <žanr>" + "\n" +
                    "Lisa film:   L <žanr> <film>" + "\n"
                    "Vaata filmi: V <vaata filmi>" + "\n"
                    "Lõpeta:      E" + "\n")
    sisend_juppideks = sisend.split()
    täht = sisend_juppideks[0]
    if täht == "K":
        žanr = sisend_juppideks[1]
        argumendid = žanr
    elif täht == "L":
        žanr = sisend_juppideks[1]
        nimi = sisend_juppideks[2:]
        nimi = " ".join(nimi)
        argumendid = [žanr, nimi]
    elif täht == "V":
        nimi = sisend_juppideks[1:]
        argumendid = " ".join(nimi)
    tagastus = ""
    def töötleKäsk(täht, argumendid):
        if täht == "K":
            valik = film.loetleFilmid(argumendid)
            while valik == []:
                valik = input("Sellise žanriga filme programm ei lednud. Proovi midagi muud: ")
                valik = film.loetleFilmid(valik)
            print("Võimalikud filmid on: ")
            print("; ".join(valik))
            tagastus = True
        elif täht == "L":
            žanr = argumendid[0]
            nimi = argumendid[1]
            film.lisaFilm(nimi, žanr)
            print("Film lisatud!")
            tagastus = True
        elif täht == "V":
            filmi_nimi = argumendid
            film.kustutaFilm(filmi_nimi)
            print("Film nimekirjast kustutatud!")
            tagastus = True
        elif täht == "E":
            tagastus = False
        return tagastus
    if töötleKäsk(täht, argumendid) == True:
        continue
    else:
        break
    