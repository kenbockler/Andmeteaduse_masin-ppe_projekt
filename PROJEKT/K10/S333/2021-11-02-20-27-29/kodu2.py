def võitja(maatriks):
    sõnastik={
        'O': 0,
        'X': 0
        }
    O_d=0
    X_d=0
    def kontroll(rida):
        O_d=0
        X_d=0
        for i in range(2):
            if rida[i:i+3] ==['O','O','O']:
                O_d+=1
                if O_d== 1:
                    sõnastik['O']= sõnastik['O']+1
                    O_d=0
            elif rida[i:i+3] ==['X','X','X']:
                X_d+=1
                if X_d== 1:
                    sõnastik['X']= sõnastik['X']+1
                    X_d=0
    for rida in maatriks:
        kontroll(rida)
    for i in range(len(maatriks)):
        veerg=[]
        for j in range(len(maatriks)):
            el= maatriks[j][i]
            veerg.append(el)
        kontroll(veerg)
        veerg.clear
    diagonaal=[]
    for i in range(len(maatriks)):
        el= maatriks[i][i]
        diagonaal.append(el)
    kontroll(diagonaal)
    diagonaal.clear
    diagonaal1=[]
    diagonaal2=[]
    for i in range(len(maatriks)-1):
        j= i+1
        el1= maatriks[i][j]
        el2= maatriks[j][i]
        diagonaal1.append(el1)
        diagonaal2.append(el2)
    kontroll(diagonaal1)
    diagonaal1.clear
    kontroll(diagonaal2)
    diagonaal2.clear
    diagonaal=[]
    for i in range(len(maatriks)):
        el= maatriks[i][-(i+1)]
        diagonaal.append(el)
    kontroll(diagonaal)
    diagonaal.clear
    diagonaal1=[]
    diagonaal2=[]
    for i in range(len(maatriks)-2,-1,-1):
        j= len(maatriks)-2 -i
        el1= maatriks[i][j]
        el2= maatriks[i+1][j+1]
        diagonaal1.append(el1)
        diagonaal2.append(el2)
    kontroll(diagonaal1)
    diagonaal1.clear
    kontroll(diagonaal2)
    diagonaal2.clear
    return sõnastik