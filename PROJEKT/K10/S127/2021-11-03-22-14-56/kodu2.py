def võitja(maatriks):
    X_loendur=0      
    O_loendur=0
    sõnastik={}
    for i in range(4):
        for j in range(4):
            if maatriks[i][j]==maatriks[i][j+1]==maatriks[i][j+2]=="X":
                X_loendur+=1
            elif maatriks[i][j]==maatriks[i+1][j]==maatriks[i+2][j]=="X":
                X_loendur+=1
            elif maatriks[i][j]==maatriks[i+1][j+1]==maatriks[i+2][j+2]=="X":
                X_loendur+=1
        sõnastik["X"]=X_loendur
        sõnastik["O"]=O_loendur
    return sõnastik         
print(võitja([["","X","X","X"],
              ["O","O","O","X"],
              ["","","","X"],
              ["O","","","X"]]))