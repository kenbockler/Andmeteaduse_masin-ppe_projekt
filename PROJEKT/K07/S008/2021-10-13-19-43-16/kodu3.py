def s�nnikuup�ev (isikukood):
    s�ne = ""
    if isikukood[5] == "0":
        s�ne += isikukood[6] + ". "
    else:
        s�ne += isikukood[5:7] + ". "
    if isikukood[3:5] == "01":
        s�ne += "jaanuar"
    elif isikukood[3:5] == "02":
        s�ne += "veebruar"
    elif isikukood[3:5] == "03":
        s�ne += "m�rts"
    elif isikukood[3:5] == "04":
        s�ne += "aprill"
    elif isikukood[3:5] == "05":
        s�ne += "mai"
    elif isikukood[3:5] == "06":
        s�ne += "juuni"
    elif isikukood[3:5] == "07":
        s�ne += "juuli"
    elif isikukood[3:5] == "08":
        s�ne += "august"
    elif isikukood[3:5] == "09":
        s�ne += "september"
    elif isikukood[3:5] == "10":
        s�ne += "oktoober"
    elif isikukood[3:5] == "11":
        s�ne += "november"
    elif isikukood[3:5] == "12":
        s�ne += "detsember"
    if int (isikukood[0]) < 3:
        s�ne += " 18" + isikukood[1:3]
    elif int (isikukood[0]) < 5:
        s�ne += " 19" + isikukood[1:3]
    elif int (isikukood[0]) < 7:
        s�ne += " 20" + isikukood[1:3]
    else:
        s�ne += " 21" + isikukood[1:3]
    return s�ne
print (s�nnikuup�ev ('34501234215'))