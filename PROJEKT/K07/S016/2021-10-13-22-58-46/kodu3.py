kuude_nimed = ["jaanuar", "veebruar", "m�rts", "aprill", "mai", "juuni", "juuli", "august", "september", "oktoober", "november", "detsember"]
def s�nnikuup�ev(isikukood):
    esimene_s�mbol = isikukood[0]
    aasta = isikukood[1:3]
    if esimene_s�mbol == "1" or esimene_s�mbol == "2":
        aasta_p�ris = "18" + aasta
        p�ev = isikukood[5:7]
        kuu = isikukood[3:5]
        if p�ev[0] == "0":
            p�ev = p�ev[1]
            if kuu[0] == "0":
                kuu = kuu[1]
                kuu_arv = kuude_nimed[int(kuu)-1]
                return p�ev + ". " + kuu_arv + " " + aasta_p�ris
            else:
                kuu = kuude_nimed[int(kuu)-1]
                return p�ev + ". " + kuu + " " + aasta_p�ris
        else:
            if kuu[0] == "0":
                kuu = kuu[1]
                kuu_arv = kuude_nimed[int(kuu)-1]
                return p�ev + ". " + kuu_arv + " " + aasta_p�ris
            else:
                kuu = kuude_nimed[int(kuu)-1]
                return p�ev + ". " + kuu + " " + aasta_p�ris
    else:
        if aasta[0] == "0" or aasta[0] == "1" or aasta[0] == "2" or aasta[0] == "5":
            aasta_p�ris = "20" + aasta
        else:
            aasta_p�ris = "19" + aasta
        p�ev = isikukood[5:7]
        kuu = isikukood[3:5]
        if p�ev[0] == "0":
            p�ev = p�ev[1]
            if kuu[0] == "0":
                kuu = kuu[1]
                kuu_arv = kuude_nimed[int(kuu)-1]
                return p�ev + ". " + kuu_arv + " " + aasta_p�ris
            else:
                kuu = kuude_nimed[int(kuu)-1]
                return p�ev + ". " + kuu + " " + aasta_p�ris
        else:
            if kuu[0] == "0":
                kuu = kuu[1]
                kuu_arv = kuude_nimed[int(kuu)-1]
                return p�ev + ". " + kuu_arv + " " + aasta_p�ris
            else:
                kuu = kuude_nimed[int(kuu)-1]
                return p�ev + ". " + kuu + " " + aasta_p�ris
print(s�nnikuup�ev("19907062285"))