def s�nnikuup�ev(ide):
    aasta = ""
    kuu = ""
    p�ev = ""
    kuud = ["jaanuar", "veebruar", "m�rts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
    if ide[0] == "1" or ide[0] == "2":
        aasta += "18"
    elif ide[0] == "3" or ide[0] == "4":
        aasta += "19"
    elif ide[0] == "5" or ide[0] == "6":
        aasta += "20"
    elif ide[0] == "7" or ide[0] == "8":
        aasta += "21"
    aasta = str(aasta + ide[1] + ide[2])
    kuu_i = int(ide[3] + ide[4]) - 1
    kuu = str(kuud[kuu_i])
    p�ev = str(ide[5] + ide[6])
    kuup�ev = p�ev + ". " + kuu + " " + aasta
    return kuup�ev