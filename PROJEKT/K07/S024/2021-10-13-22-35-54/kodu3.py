s�ne = []
def s�nnikuup�ev(isikukood):
    j�rjend = list(isikukood)
    p�ev = "".join(j�rjend[5:7])
    kuu_nr = j�rjend[3:5]
    if j�rjend[3] == "0" and j�rjend[4]=="1":
        kuu_s�naga = "jaanuar"
    elif j�rjend[3] == "0" and j�rjend[4]=="2":
        kuu_s�naga = "veebruar"
    elif j�rjend[3] == "0" and j�rjend[4]=="3":
        kuu_s�naga = "m�rts"
    elif j�rjend[3] == "0" and j�rjend[4]=="4":
        kuu_s�naga = "aprill"
    elif j�rjend[3] == "0" and j�rjend[4]=="5":
        kuu_s�naga = "mai"
    elif j�rjend[3] == "0" and j�rjend[4]=="6":
        kuu_s�naga = "juuni"
    elif j�rjend[3] == "0" and j�rjend[4]=="7":
        kuu_s�naga = "juuli"
    elif j�rjend[3] == "0" and j�rjend[4]=="8":
        kuu_s�naga = "august"
    elif j�rjend[3] == "0" and j�rjend[4]=="9":
        kuu_s�naga = "september"
    elif j�rjend[3] == "1" and j�rjend[4]=="0":
        kuu_s�naga = "oktoober"
    elif j�rjend[3] == "1" and j�rjend[4]=="1":
        kuu_s�naga = "november"    
    elif j�rjend[3] == "1" and j�rjend[4]=="2":
        kuu_s�naga = "detsember"
    aasta_l�pp = "".join(j�rjend[1:3])
    if j�rjend[0] == "1" or j�rjend[0] == "2":
            aasta = "18" + aasta_l�pp
    elif j�rjend[0] == "3" or j�rjend[0] == "4":
            aasta = "19" + str(aasta_l�pp)
    elif j�rjend[0] == "5" or j�rjend[0] == "6":
            aasta = "20" + aasta_l�pp
    return p�ev + "." + " " + kuu_s�naga + " " + aasta
