a = input("Sisestage isikukood: ")
def s�nnikuup�ev(a):
    kuud = ["jaanuar","veebruar","m�rts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
    kuunumber = int(a[3:5])
    kuu  = kuud[kuunumber -1]
    if a[0] == 6 or a[0] == 5:
        aasta = "20"+a[1:3]
        p�ev = a[5:7]
        v�ljund = (p�ev+". "+kuu+" "+aasta)
        return v�ljund
    else:
        aasta = "19"+a[1:3]
        p�ev = a[5:7]
        v�ljund = (p�ev+". "+kuu+" "+aasta)
        return v�ljund