def transponeeriK(maatriks):
    x = len(maatriks[0])
    y = len(maatriks)
    T_maatriks = []
    t_x = [0] * y
    for t_y in range(x):
        T_maatriks.append(t_x.copy())
    x_index = -1 
    for i in range(y):
        y_index = -1
        for j in range(x):
            T_maatriks[y_index][x_index] = maatriks[i][j]
            y_index -= 1
        x_index -= 1
    return T_maatriks
transponeeriK([[1, 2], [3, 4], [5, 6], [7, 8]])