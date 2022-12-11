def loetleFilmid(žanri_nimetus):
    fail = open("filmid.txt", encoding="UTF-8")
    for rida in fail:
        fail.readline().strip
        rida = rida.split(" - ")
def lisaFilm(filmi_nimi, žanri_nimetus):
    fail = open('filmid.txt', "a", encoding="utf-8")
    fail.write("\n")
    fail.write(filmi_nimi + " - ")
    fail.write(žanri_nimetus)
    fail.close()
def kustutaFilm(filmi_nimi):
    fail = open('filmid.txt', "r")
    lines = fail.readlines()
    fail.close()
    with open("filmid.txt", "w") as fail:
        for line in lines:
            if line.strip('\n') != filmi_nimi:
                fail.write(line)
file = open("filmid.txt", encoding="UTF-8")
for rida in file:
    file.readline().strip
    rida = rida.split(" - ")
    print(rida)
  