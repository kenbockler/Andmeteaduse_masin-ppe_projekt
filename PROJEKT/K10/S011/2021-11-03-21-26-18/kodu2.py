def v�itja(maatriks):
    m�ngu_seis = {}
    x = 0
    o = 0
    if maatriks[0][0]== maatriks[0][1] == maatriks[0][2] == "X" :
        x += 1
    if maatriks[0][1] == maatriks[0][2] == maatriks[0][3] == "X":
        x += 1
    if maatriks[1][0]== maatriks[1][1] == maatriks[1][2] == "X" :
        x += 1
    if maatriks[1][1] == maatriks[1][2] == maatriks[1][3] == "X":
        x += 1
    if maatriks[2][0]== maatriks[2][1] == maatriks[2][2] == "X" :
        x += 1
    if maatriks[2][1] == maatriks[2][2] == maatriks[2][3] == "X":
        x += 1
    if maatriks[3][0]== maatriks[3][1] == maatriks[3][2] == "X" :
        x += 1
    if maatriks[3][1] == maatriks[3][2] == maatriks[3][3] == "X":
        x += 1
    if maatriks[0][0]== maatriks[1][0] == maatriks[2][0] == "X" :
        x += 1
    if maatriks[1][0] == maatriks[2][0] == maatriks[3][0] == "X":
        x += 1
    if maatriks[0][1] == maatriks[1][1] == maatriks[2][1] == "X":
        x += 1
    if maatriks[1][1] == maatriks[2][1] == maatriks[3][1] == "X":
        x += 1
    if maatriks[0][2] == maatriks[1][2] == maatriks[2][2] == "X":
        x += 1
    if maatriks[1][2] == maatriks[2][2] == maatriks[3][2] == "X":
        x += 1
    if maatriks[0][3] == maatriks[1][3] == maatriks[2][3] == "X":
        x += 1
    if maatriks[1][3] == maatriks[2][3] == maatriks[3][3] == "X":
        x += 1
    if maatriks[0][0] == maatriks[1][1] == maatriks[2][2] == "X" :
        x += 1
    if maatriks[1][1] == maatriks[2][2] == maatriks[3][3] == "X" :
        x += 1
    if maatriks[0][3] == maatriks[1][2] == maatriks[2][1] == "X" :
        x += 1
    if maatriks[1][2] == maatriks[2][1] == maatriks[3][0] == "X" :
        x += 1
    if maatriks[1][0] == maatriks[2][1] == maatriks[3][2] == "X":
        x += 1
    if maatriks[0][1] == maatriks[1][2] == maatriks[2][3] == "X" :
        x += 1      
    if maatriks[1][3] == maatriks[2][2] == maatriks[3][1] == "X":
        x += 1
    if maatriks[0][2] == maatriks[1][1] == maatriks[2][0] == "X" :
        x += 1
    if maatriks[0][0]== maatriks[0][1] == maatriks[0][2] == "O" :
        o += 1
    if maatriks[0][1] == maatriks[0][2] == maatriks[0][3] == "O":
        o += 1
    if maatriks[1][0]== maatriks[1][1] == maatriks[1][2] == "O" :
        o += 1
    if maatriks[1][1] == maatriks[1][2] == maatriks[1][3] == "O":
        o += 1
    if maatriks[2][0]== maatriks[2][1] == maatriks[2][2] == "O" :
        o += 1
    if maatriks[2][1] == maatriks[2][2] == maatriks[2][3] == "O":
        o += 1
    if maatriks[3][0]== maatriks[3][1] == maatriks[3][2] == "O" :
        o += 1
    if maatriks[3][1] == maatriks[3][2] == maatriks[3][3] == "O":
        o += 1
    if maatriks[0][0]== maatriks[1][0] == maatriks[2][0] == "O" :
        o += 1
    if maatriks[1][0] == maatriks[2][0] == maatriks[3][0] == "O":
        o += 1
    if maatriks[0][1] == maatriks[1][1] == maatriks[2][1] == "O":
        o += 1
    if maatriks[1][1] == maatriks[2][1] == maatriks[3][1] == "O":
        o += 1
    if maatriks[0][2] == maatriks[1][2] == maatriks[2][2] == "O":
        o += 1
    if maatriks[1][2] == maatriks[2][2] == maatriks[3][2] == "O":
        o += 1
    if maatriks[0][3] == maatriks[1][3] == maatriks[2][3] == "O":
        o += 1
    if maatriks[1][3] == maatriks[2][3] == maatriks[3][3] == "O":
        o += 1
    if maatriks[0][0] == maatriks[1][1] == maatriks[2][2] == "O" :
        o += 1
    if maatriks[1][1] == maatriks[2][2] == maatriks[3][3] == "O" :
        o += 1
    if maatriks[0][3] == maatriks[1][2] == maatriks[2][1] == "O" :
        o += 1
    if maatriks[1][2] == maatriks[2][1] == maatriks[3][0] == "O" :
        o += 1
    if maatriks[1][0] == maatriks[2][1] == maatriks[3][2] == "O":
        o += 1
    if maatriks[0][1] == maatriks[1][2] == maatriks[2][3] == "O" :
        o += 1   
    if maatriks[1][3] == maatriks[2][2] == maatriks[3][1] == "O":
        o += 1
    if maatriks[0][2] == maatriks[1][1] == maatriks[2][0] == "O" :
        o += 1
    m�ngu_seis["O"] = o
    m�ngu_seis["X"] = x
    return (m�ngu_seis)