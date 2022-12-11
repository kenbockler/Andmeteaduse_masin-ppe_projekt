def seosta_lapsed_ja_vanemad(lapsed, nimed):
    lastefail = open(lapsed, encoding = "UTF-8")
    nimedefail = open(nimed, encoding = "UTF-8")
    tulemuss�nastik = {}
    s�nastik = {}
    for nimirida in nimedefail:
        nimedej�rjend = nimirida.strip().split(" ")
        s�nastik[nimedej�rjend[0]] = nimedej�rjend[1] + " " + nimedej�rjend[2]
    for isikukoodid in lastefail:
        isikutej�rjend = isikukoodid.strip().split(" ")
        vanem = s�nastik[isikutej�rjend[0]]
        laps = s�nastik[isikutej�rjend[1]]
        if laps in tulemuss�nastik:
            tulemuss�nastik[laps].add(vanem)
        else:
            tulemuss�nastik[laps] = set()
            tulemuss�nastik[laps].add(vanem)
    return tulemuss�nastik
seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")