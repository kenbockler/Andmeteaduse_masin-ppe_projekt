def s�nnikuup�ev(ik):
    p�ev = ik[5:7]
    esimene_nr = ik[0]
    if esimene_nr == 1:
        aasta = "18" + ik[1:3]
    elif esimene_nr == 2:
        aasta = "18" + ik[1:3]
    elif esimene_nr == 3:
        aasta = "19" + ik[1:3]
    elif esimene_nr == 4:
        aasta = "19" + ik[1:3]
    else:
        aasta = "20" + ik[1:3]
    kuu_nr = ik[3:5]
    if kuu_nr == '01':
        kuu = "jaanuar"
    elif kuu_nr == '02':
        kuu = "veebruar"
    elif kuu_nr == '03':
        kuu = "m�rts"
    elif kuu_nr == '04':
        kuu = "aprill"
    elif kuu_nr == '05':
        kuu = "mai"
    elif kuu_nr == '06':
        kuu = "juuni"
    elif kuu_nr == '07':
        kuu = "juuli"
    elif kuu_nr == '08':
        kuu = "august"
    elif kuu_nr == '09':
        kuu = "september"
    elif kuu_nr == '10':
        kuu = "oktoober"
    elif kuu_nr == '11':
        kuu = "november"
    else:
        kuu = "detsember"
    print(p�ev + ". " + kuu + " " + aasta)
ik = input("Sisesta oma isikukood: ")
s�nnikuup�ev(ik)
    