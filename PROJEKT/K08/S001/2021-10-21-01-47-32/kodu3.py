import film
def t��tleK�sk(taht,argumendid):
    if taht == "K":
        print("V�imalikud filmid on: ")
        for filminimi in film.loetleFilmid(argumendid[0]):
            print(filminimi)
    if taht == "L":
        film.lisaFilm(argumendid[1], argumendid[0])
        print("Film lisatud!")
    if taht == "V":
        film.kustutaFilm(argumendid[0])
        print("Film nimekirjast kustutatud!")
        print("Head vaatamist!")
    if taht == "E":
        return False
    return True
print("====== FILMIANDMEBAAS ======")
print("Kuva filmid: K <�anr>")
print("Lisa film:   L <�anr> <film>")
print("Vaata filmi: V <filmi nimi>")
print("L�peta:      E")
print("============================")
jatka = True
while jatka == True:
    andmed = input()
    andmed = andmed.split(" ", 1)
    argumendid = []
    if andmed[0] == "L":
        argumendid.extend(andmed[1].split(" ", 1))
    elif andmed[0] == "K" or andmed[0] == "V":
        argumendid.append(andmed[1])
    taht = andmed[0]
    jatka = t��tleK�sk(taht, argumendid)