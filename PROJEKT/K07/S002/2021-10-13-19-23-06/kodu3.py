kuud = ["jaanuar","veebruar","m�rts","aprill","mai","juuni","juuli","august","september","oktoober","november","detsember"]
aasta = [18,18,19,19,20,20]
def s�nnikuup�ev(x):
    global kuud
    global aasta
    return str(x[5:7])+". "+str(kuud[int(x[3:5])-1])+" "+str(aasta[int(x[0])-1])+str(x[1:3])
print(s�nnikuup�ev('34501234215'))