kombinatsioonid = []
sõnastik ={}
def võitja(järjend):
    for i in range(4):
        for j in range(2):
            kombinatsioonid.append(maatriks[i][j]+maatriks[i][j+1]+maatriks[i][j+2])
    for i in range(4):
        for j in range(2):
            kombinatsioonid.append(maatriks[j][i]+maatriks[j+1][i]+maatriks[j+2][i])
    for i in range(2):
        kombinatsioonid.append(maatriks[i][i]+maatriks[i+1][i+1]+maatriks[i+2][i+2])
    for i in range(1):
        kombinatsioonid.append(maatriks[i][i+1]+maatriks[i+1][i+2]+maatriks[i+2][i+3])
    for i in range(1):
        kombinatsioonid.append(maatriks[i+1][i]+maatriks[i+2][i+1]+maatriks[i+3][i+2])
    for i in range(2):
        kombinatsioonid.append(maatriks[3-i][i]+maatriks[2-i][i+1]+maatriks[1-i][i+2])
    for i in range(1):
        kombinatsioonid.append(maatriks[2-i][i]+maatriks[1-i][i+1]+maatriks[0-i][i+2])
    for i in range(1):
        kombinatsioonid.append(maatriks[3-i][i+1]+maatriks[2-i][i+2]+maatriks[1-i][i+3])
    for el in kombinatsioonid:
            if (el == "XXX" or el == "OOO"):
                sõnastik[el] = sõnastik.get(el, 0) + 1
    return sõnastik
maatriks = [
    ['O',' ','O','X'],
    ['O','O','X','X'],
    ['O','X','O',' '],
    ['X','X','X','O']
    ]
print(võitja(maatriks))