import numpy as np
def transponeeriK (maatriks):
    transponeeritud_maatriks = maatriks.transpose()
    õige = transponeeritud_maatriks[::-1]
    return õige
maatriks = np.array ([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(transponeeriK(maatriks))
maatriks = [[1, 2],
            [3, 4],
            [5, 6],
            [7, 8]]