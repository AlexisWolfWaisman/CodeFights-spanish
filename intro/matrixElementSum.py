def matrixElementsSum(matrix):
    i = len(matrix)
    j = len(matrix[0])
    total = 0
    for y in range(0, j):
        vector = []
        for x in range(0,i):
            vector.append(matrix[x][y])
        for elem in vector:
            if elem == 0:
                break
            else:
                total += elem
    return total





prueba1 = [[0, 1, 1, 2],[0, 5, 0, 0],[2, 0, 3, 3]]
prueba2 = [[1,1,1,0],[0,5,0,1],[2,1,3,10]]
print(matrixElementsSum(prueba1))
print(matrixElementsSum(prueba2))
