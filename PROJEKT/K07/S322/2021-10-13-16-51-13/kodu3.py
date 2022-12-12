def sünnikuupäev(isikukood):
    sajandjasugu = int(isikukood[0])
    aastatuhat = 1800 + int((sajandjasugu-1) / 2) * 100
    sünniaasta = isikukood[1:3]
    if sünniaasta[0] == "0":
        sünniaasta = int(sünniaasta[1:])
    else:
        sünniaasta = int(sünniaasta)
    sünniaasta += aastatuhat
    kuud = ("jaanuar", "veebruar", "märts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember")
    kuu = isikukood[3:5]
    if kuu[0] == "0":
        kuu = kuud[int(kuu[-1])-1]
    else:
        kuu = kuud[int(kuu)-1]
    päev = isikukood[5:7]
    if päev[0] == "0":
        päev = päev[-1]
    return str(päev) + ". " + kuu + " " + str(sünniaasta)
