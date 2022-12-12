def transponeeriK(matrix):
    return [[matrix[len(matrix)-1-j][len(matrix[0])-1-i] for j in range(len(matrix))] for i in range(len(matrix[0]))]