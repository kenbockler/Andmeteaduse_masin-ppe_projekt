def sünnikuupäev(isik):
    list(isik)
    kuu = isik[3:5]
    aasta = isik[1:3]
    kuu1 = ("")
    if isik[:1] == '3' or isik[:1] == '4':
        aasta = "19" + isik[1:3]
    if isik[:1] == '5' or isik[:1] == '6':
        aasta = "20" + isik[1:3]
    if isik[5] == "0":
        päev = isik[6]
    else:
        päev = isik[5:7]
    if kuu == "1":
        kuu1 = "jaanuar"
    if kuu == "2":
        kuu1 = "vebruaar"
    if kuu == "3":
        kuu1 = "märts"
    if kuu == "4":
        kuu1 = "aprill"
    if kuu == "5":
        kuu1 = "mai"
    if kuu == "6":
        kuu1 = "juuni"
    if kuu == "7":
        kuu1 = "juuli"
    if kuu == "8":
        kuu1 = "jaanuar"
    if kuu == "9":
        kuu1 = "august"
    if kuu == "10":
        kuu1 = "september"
    if kuu == "11":
        kuu1 = "oktoober"
    if kuu == 1:
        kuu1 = "november"
    if kuu == "12":
        kuu1 = "detsember"
    return päev + ". " + kuu1 + " " + aasta
        