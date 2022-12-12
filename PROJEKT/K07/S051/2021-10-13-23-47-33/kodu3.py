def sünnikuupäev(isikukood):
    kuude_loetelu = ["jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    päev = ""
    kuu_nimi = ""
    aasta = ""
    if isikukood[0] in "12":
        aasta = "18"
    elif isikukood[0] in "34":
        aasta = "19"
    elif isikukood[0] in "56":
        aasta = "20"
    elif isikukood[0] in "78":
        aasta = "21"
    aasta += isikukood[1] + isikukood[2]
    kuu_indeks = int(isikukood[3] + isikukood[4]) - 1
    kuu_nimi = kuude_loetelu[kuu_indeks] + " "
    päev = isikukood[5] + isikukood[6] + ". "
    return päev + kuu_nimi + aasta