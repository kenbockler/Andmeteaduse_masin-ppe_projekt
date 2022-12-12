def sünnikuupäev(isikukood):
    sünniaasta = str(isikukood)[1:3]
    sünnikuu = str(isikukood)[3:5]
    päev = str(isikukood)[5:7]
    if str(isikukood)[0] == "1" or str(isikukood)[0] == "2":
        aasta = "18" + sünniaasta
    elif  str(isikukood)[0] == "3" or str(isikukood)[0] == "4":
        aasta = "19" + sünniaasta
    elif  str(isikukood)[0] == "5" or str(isikukood)[0] == "6":
        aasta = "20" + sünniaasta
    if sünnikuu == "01":
        kuu = "jaanuar"
    elif sünnikuu == "02":
        kuu = "veebruar"
    elif sünnikuu == "03":
        kuu = "märts"
    elif sünnikuu == "04":
        kuu = "aprill"
    elif sünnikuu == "05":
        kuu = "mai"
    elif sünnikuu == "06":
        kuu = "juuni"
    elif sünnikuu == "07":
        kuu = "juuli"
    elif sünnikuu == "08":
        kuu = "august"
    elif sünnikuu == "09":
        kuu = "september"
    elif sünnikuu == "10":
        kuu = "oktoober"
    elif sünnikuu == "11":
        kuu = "november"
    elif sünnikuu == "12":
        kuu = "detsember"
    return str(päev) + ". " + kuu + " " + aasta
