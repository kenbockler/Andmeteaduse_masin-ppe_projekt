def sünnikuupäev(id_sõne):
    l = list(id_sõne)
    sugu = l[0]
    if sugu in ("1", "2"):
        aasta = "18"
    elif sugu in ("3", "4"):
        aasta = "19"
    elif sugu in ("5", "6"):
        aasta = "20"
    else:
        aasta = "21"
    aasta += l[1]+l[2]
    kuu = l[3]+l[4]
    kuud = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni"]
    kuud += ["juuli", "august", "september", "oktoober", "november", "detsember"]
    for k in kuud:
        if int(kuu) ==  kuud.index(k) + 1:
            kuu_nimi = k
    kuupäev = l[5]+l[6]
    return("{0}. {1} {2}".format(kuupäev, kuu_nimi, aasta))