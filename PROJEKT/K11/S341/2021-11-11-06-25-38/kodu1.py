def seosta_lapsed_ja_vanemad(fail1, fail2):
    i= 0
    j= 0
    sõnastik = {}
    fail1 = open('nimed.txt')
    fail2 = open('lapsed.txt')
    for rida in fail1:
        Rida= rida.split(' ')
        isikukood= Rida[0]
        nimi= Rida[1:3]
        isikukood, nimi = Rida
        sõnastik[isikukood] = nimi
    for rida in fail2:
        eraldatudRida = rida.split(' ')
        vanematekood = int(eraldatudRida[0])
        lastekood = int(eraldatudRida[1])
seosta_lapsed_ja_vanemad('lapsed.txt','nimed.txt')
    