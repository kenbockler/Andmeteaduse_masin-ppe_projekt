def s�nnikuup�ev(isikukood):
    kuud = ["jaanuar", "veebruar", "m�rts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kood = list(isikukood)
    if int(kood[5]) > 0:
        kuup�ev = kood[5] + kood[6]
    else:
        kuup�ev = isikukood[6]
    if int(kood[3]) > 0:
        if int(kood[4]) == 1:
            kuu = kuud[10]
        elif int(kood[4]) == 2:
            kuu = kuud[11]
        else:
            kuu = kuud[9]
    else:
        kuu = kuud[int(kood[4]) - 1]
    if int(kood[0]) < 3:
        aasta = "18" + kood[1] + kood[2]
    elif int(kood[0]) < 5:
        aasta = "19" + kood[1] + kood[2]
    else:
        aasta = "20" + kood[1] + kood[2]
    kuup�ev_kuu_aasta = (kuup�ev + ". " + kuu + " " + aasta)
    return kuup�ev_kuu_aasta
isikukood = '29802158384'
print(s�nnikuup�ev(isikukood))