def esinemiste_arv(maatriks, sümbol):
    kokku = 0
    for i in range(len(maatriks)):
        for j in range(len(maatriks[i]) - 2):
            if maatriks[i][j] == maatriks[i][j + 1] == maatriks[i][j + 2] == sümbol:
                kokku += 1
    for i in range(len(maatriks) - 2):
        for j in range(len(maatriks[i])):
            if maatriks[i][j] == maatriks[i + 1][j] == maatriks[i + 2][j] == sümbol:
                kokku += 1
    for i in range(len(maatriks) - 2):
        for j in range(len(maatriks[i]) - 2):
            if maatriks[i][j] == maatriks[i + 1][j + 1] == maatriks[i + 2][j + 2] == sümbol:
                kokku += 1
    for i in range(len(maatriks) -  2):
        for j in range(2, len(maatriks[i])):
            if maatriks[i][j] == maatriks[i + 1][j - 1] == maatriks[i + 2][j - 2] == sümbol:
                kokku += 1
    return kokku
def võitja(maatriks):
    O = esinemiste_arv(maatriks, "O")
    X = esinemiste_arv(maatriks, "X")
    return {"O": O, "X": X}
print(võitja([['O',' ','O','X'],
            ['O','O','X','X'],
            ['O','X','O',' '],
            ['X','X','X','O']]))
