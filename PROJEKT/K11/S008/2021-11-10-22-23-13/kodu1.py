fail1 = open("lapsed.txt", "r")
fail2 = open("nimed.txt", "r")
def seosta_lapsed_ja_vanemad(fail1, fail2):
    s�nastik = {}
    lapsedjavanemad = {}
    viimane = {}
    for rida in fail2:
        rida1 =rida.split()
        nimi = rida1[1] + " " + rida1[2]
        s�nastik[rida1[0]]= nimi
    for rida in fail1:        
        rida2 = rida.split()
        vanem= rida2[0]
        laps= rida2[1]
        vanemad = lapsedjavanemad.get(laps, set())
        vanemad.add(vanem)
        lapsedjavanemad[laps] = vanemad
    for key in lapsedjavanemad.keys():
        v�ti = s�nastik.get(key)
        b = set()
        for el in lapsedjavanemad.get(key):
            b.add(s�nastik.get(el))
        viimane[v�ti] = b
    return viimane
print(seosta_lapsed_ja_vanemad(fail1, fail2))
fail1.close()
fail2.close()