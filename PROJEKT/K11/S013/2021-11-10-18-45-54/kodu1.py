def seosta_lapsed_ja_vanemad(x,y):
    lapsed = open(x)
    nimed = open(y) 
    s�nastik1 = {}
    s�nastik2 = {}
    for rida in nimed:
        rida = rida.strip("\n")
        rida = rida.split(" ", 1)
        s�nastik1[rida[0]] = rida[1]
    for rida in lapsed:
        rida = rida.strip("\n")
        rida = rida.split(" ")
        lapsenimi = s�nastik1[rida[1]]
        vanemanimi = s�nastik1[rida[0]]
        if lapsenimi in s�nastik2:
            s�nastik2[lapsenimi].add(vanemanimi)
        else:
            s�nastik2[lapsenimi] = set()
            s�nastik2[lapsenimi].add(vanemanimi)
    return s�nastik2
print(seosta_lapsed_ja_vanemad("lapsed.txt","nimed.txt"))