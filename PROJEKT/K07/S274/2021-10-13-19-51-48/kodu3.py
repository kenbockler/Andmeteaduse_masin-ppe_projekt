def sünnikuupäev(isikukood):
    kuupäev = isikukood[5:7]
    if isikukood[3:5] == "01":
        kuu = "jaanuar"
    elif isikukood[3:5] == "02":
        kuu = "veebruar"
    elif isikukood[3:5] == "03":
        kuu = "märts"
    elif isikukood[3:5] == "04":
        kuu = "aprill"
    elif isikukood[3:5] == "05":
        kuu = "mai"
    elif isikukood[3:5] == "06":
        kuu = "juuni"
    elif isikukood[3:5] == "07":
        kuu = "juuli"
    elif isikukood[3:5] == "08":
        kuu = "august"
    elif isikukood[3:5] == "09":
        kuu = "september"
    elif isikukood[3:5] == "10":
        kuu = "oktoober"
    elif isikukood[3:5] == "11":
        kuu = "november"
    elif isikukood[3:5] == "12":
        kuu = "detsember"
    if isikukood[0] == "1" or isikukood[0] == "2":
        aasta = "18" + isikukood[1:3]
    elif isikukood[0] == "3" or isikukood[0] == "4":
        aasta = "19" + isikukood[1:3]
    elif isikukood[0] == "5" or isikukood[0] == "6":
        aasta = "20" + isikukood[1:3]
    return(kuupäev + ". " + kuu + " " + aasta)
sünnikuupäev('34501234125')
