def odavaim_takso(teepikkus):
    nimi = []
    sissehind = []
    kmhind = []
    vastav_hinnad = []
    nimed = []
    f = open('taksohinnad.txt')
    for rida in f:
        jupid = rida.split(',')
        nimi = jupid[0]
        nimed += [nimi]
        sissehind = float(jupid[1])
        kmhind = float(jupid[2].strip())
        koguhind = float(sissehind + teepikkus * kmhind)
        vastav_hinnad += [koguhind]    
    f.close()
    try:
        odavaim_hind = min(vastav_hinnad)
        indeks = vastav_hinnad.index(odavaim_hind)
        odavaim_nimi = nimed[indeks]
        print('Kõige odavam on', odavaim_nimi)
    except:
        print('Ei saa arvutada')
teepikkus = float(input('Sisesta tee pikkus kilomeetrites: '))
odavaim_takso(teepikkus)