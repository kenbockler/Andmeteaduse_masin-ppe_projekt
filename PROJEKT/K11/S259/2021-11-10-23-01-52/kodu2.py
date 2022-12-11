import numpy as np
def transponeeriK(maatriks):
    matrix = np.array(maatriks)
    matrix = matrix[::-1]
    matrix = matrix.transpose()
    matrix = matrix[::-1]
    return matrix.tolist()
