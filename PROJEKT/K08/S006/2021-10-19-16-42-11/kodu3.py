import film
while True:
    sisend = input( "\n" +
                    "Kuva filmid: K <�anr>" + "\n" +
                    "Lisa film:   L <�anr> <film>" + "\n"
                    "Vaata filmi: V <vaata filmi>" + "\n"
                    "L�peta:      E" + "\n")
    sisend_juppideks = sisend.split()
    t�ht = sisend_juppideks[0]
    if t�ht == "K":
        �anr = sisend_juppideks[1]
        argumendid = �anr
    elif t�ht == "L":
        �anr = sisend_juppideks[1]
        nimi = sisend_juppideks[2:]
        nimi = " ".join(nimi)
        argumendid = [�anr, nimi]
    elif t�ht == "V":
        nimi = sisend_juppideks[1:]
        argumendid = " ".join(nimi)
    tagastus = ""
    def t��tleK�sk(t�ht, argumendid):
        if t�ht == "K":
            valik = film.loetleFilmid(argumendid)
            while valik == []:
                valik = input("Sellise �anriga filme programm ei lednud. Proovi midagi muud: ")
                valik = film.loetleFilmid(valik)
            print("V�imalikud filmid on: ")
            print("; ".join(valik))
            tagastus = True
        elif t�ht == "L":
            �anr = argumendid[0]
            nimi = argumendid[1]
            film.lisaFilm(nimi, �anr)
            print("Film lisatud!")
            tagastus = True
        elif t�ht == "V":
            filmi_nimi = argumendid
            film.kustutaFilm(filmi_nimi)
            print("Film nimekirjast kustutatud!")
            tagastus = True
        elif t�ht == "E":
            tagastus = False
        return tagastus
    if t��tleK�sk(t�ht, argumendid) == True:
        continue
    else:
        break
    