def s�nnikuup�ev(isikukood):
    sajand = isikukood[0]
    if sajand == "1" or sajand == "2":
        s�nnisajand = "18"
    elif sajand == "3" or sajand == "4":
        s�nnisajand = "19"
    elif sajand == "5" or sajand == "6":
        s�nnisajand = "20"
    s�nniaasta = isikukood[1] + isikukood[2]
    s�nnikuu = isikukood[3] + isikukood[4]
    s�nnikuup�ev = isikukood[5] + isikukood[6]
    if s�nnikuu == "01":
        s�nnikuu = "jaanuar"
    elif s�nnikuu == "02":
        s�nnikuu = "veebruar"
    elif s�nnikuu == "03":
        s�nnikuu = "m�rts"
    elif s�nnikuu == "04":
        s�nnikuu = "aprill"
    elif s�nnikuu == "05":
        s�nnikuu = "mai"
    elif s�nnikuu == "06":
        s�nnikuu = "juuni"
    elif s�nnikuu == "07":
        s�nnikuu = "juuli"
    elif s�nnikuu == "08":
        s�nnikuu = "august"
    elif s�nnikuu == "09":
        s�nnikuu = "september"
    elif s�nnikuu == "10":
        s�nnikuu = "oktoober"
    elif s�nnikuu == "11":
        s�nnikuu = "november"
    elif s�nnikuu == "12":
        s�nnikuu = "detsember"
    return(s�nnikuup�ev + ". " + s�nnikuu + " " + s�nnisajand + s�nniaasta)
s�nnikuup�ev('39910122345')
            