def s�nnikuup�ev(isikukood):
    p�ev= str(isikukood[5:7])
    kuu = int(isikukood[3:5])
    kuu_j�rjend= ["jaanuar", "veebruar","m�rts","aprill","mai","juuni","juuli","\n"
                  "august","september","oktoober","november","detsember"]
    kuu= str(kuu_j�rjend[kuu-1])
    sajand = int(isikukood[0])
    if sajand <3:
        sajand = 18
    elif 3 <=sajand <5:
        sajand = 19
    elif sajand >=5:
        sajand = 20
    s�nniaasta = str(sajand)+isikukood[1:3]
    s�nnikuup�ev = p�ev +". "+ kuu + " "+ s�nniaasta
    return s�nnikuup�ev
print(s�nnikuup�ev("34501234215"))