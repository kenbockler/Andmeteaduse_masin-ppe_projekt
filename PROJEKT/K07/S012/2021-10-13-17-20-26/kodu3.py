def s�nnikuup�ev(isikukood):
    aastavahemik = isikukood[0:1]
    if aastavahemik == "1" or aastavahemik == "2":
        aasta = "18"+isikukood[1:3]
    elif aastavahemik == "3" or aastavahemik == "4":
        aasta = "19"+isikukood[1:3]
    elif aastavahemik == "5" or aastavahemik == "6":
        aasta = "20"+isikukood[1:3]
    kuu = isikukood[3:5]
    p�ev = isikukood[5:7]+"."
    if kuu == "01":
        kuu = "jaanuar"
    elif kuu == "02":
        kuu = "veebruar"
    elif kuu == "03":
        kuu = "m�rts"
    elif kuu == "04":
        kuu = "aprill"
    elif kuu == "05":
        kuu = "mai"
    elif kuu == "06":
        kuu = "juuni"
    elif kuu == "07":
        kuu = "juuli"
    elif kuu == "08":
        kuu = "august"
    elif kuu == "09":
        kuu = "september"
    elif kuu == "10":
        kuu = "oktoober"
    elif kuu == "11":
        kuu = "november"
    elif kuu == "12":
        kuu = "detsember"
    return "".join([p�ev, " ", kuu, " ", aasta])
