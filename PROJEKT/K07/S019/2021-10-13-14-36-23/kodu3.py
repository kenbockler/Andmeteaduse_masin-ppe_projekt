def s�nnikuup�ev(isikukood):
    isikukood2 = str(isikukood)
    error = ""
    if int(isikukood2[0]) == 3 or int(isikukood2[0]) == 4:
        saj = 1900
    elif int(isikukood[0]) == 5 or int(isikukood[0]) == 6:
        saj = 2000
    aasta = saj + int(isikukood2[1]) * 10 + int(isikukood[2])
    kuu = int(isikukood2[3]) * 10 + int(isikukood2[4])
    kuud = ["jaanuar","veebruar", "m�rts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    kuu_s�ne = kuud[kuu -1]
    p�ev = int(isikukood2[5]) * 10 + int(isikukood2[6])
    p�ev_punktiga = str(p�ev) + "."
    vastus = p�ev_punktiga + " " + kuu_s�ne + " " + str(aasta)
    return vastus