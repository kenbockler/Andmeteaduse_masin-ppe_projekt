read = open("filmid.txt", "r", encoding = "utf-8")
outfile = open("filmid.txt", "a", encoding = "utf-8")
nimekiri = read.readlines()
read.close()
def loetlefilmid(zanr):
    rlist = []
    for row in nimekiri:
        if row[-1:] == "\n":
            ns = row[:-1]
        else:
            ns = row
        a = ns.split(" - ")
        if a[1] == zanr:
            rlist.append(a[0])
    return rlist
print(nimekiri)
def lisafilm(nimi, zanr):
    outfile.write("\n" + nimi + " - " + zanr)
def kustutafilm(nimi):
    for row in nimekiri:
        if row[-1:] == "\n":
            ns = row[:-1]
        else:
            ns = row
        a = ns.split(" - ")
        if a[0] == nimi:
            s = 0
a = 0
outfile.close()