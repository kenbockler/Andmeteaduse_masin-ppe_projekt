vahemaa = float(input("Mitu kilomeetrit soovite te s6ita? "))
def hinnakiri(failinimi):
    firmanimi = []
    sisseastumine= []
    kilomeeter = []
    maksumus = 0
    f = open("taksohinnad.txt")
    for rida in f:
        osad = rida.split(" ")
        firmanimi = osad[0]
        sisseistumine = osad[1]
        kilomeeter = osad[2]
        maksumus = float(sisseistumine) + float(kilomeeter) * float(vahemaa)
    f.close()
    return (firmanimi, maksumus)
(firmanimi, sisseistumine, kilomeeter) = hinnakiri("taksohinnad.txt")
print("Sisestatud vahemaa oli :" + float(str(vahemaa)))
print("Odavaim taksofirma selleks s6iduks on: " + nimi)
print("S6idu hind oleks:" + float(maksumus))