maatriks = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
def transponeeriK(maatriks):
    järjend = []
    for i in range(len(maatriks[0])):
        rida = []
        for j in range(len(maatriks)):
            element = maatriks[j][i]
            rida.append(element)
        järjend.append(rida)
    return järjend
print(transponeeriK(maatriks))