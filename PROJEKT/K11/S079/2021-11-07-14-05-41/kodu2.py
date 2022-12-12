maatriks = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
oodatav = [[8, 6, 4, 2],
           [7, 5, 3, 1]]
def transponeeriK(maatriks):
    m = []
    ridade_arv = len(maatriks)
    veergude_arv = len(maatriks[0])
    for i in range(veergude_arv-1,-1,-1):
        veerud = []
        for j in range(ridade_arv-1,-1,-1):
          veerud.append(maatriks[j][i])
        m.append(veerud)
    return m