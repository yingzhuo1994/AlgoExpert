def riverSizes(matrix):
    # Write your code here.
    lengthLst = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 :
                length = lookRiver(matrix, i, j)
                lengthLst.append(length)
    return lengthLst
    

def lookRiver(matrix, x, y):
    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == 1:
        matrix[x][y] = 'X'
        result = lookRiver(matrix, x + 1, y) + lookRiver(matrix, x - 1, y)\
             + lookRiver(matrix, x, y + 1) + lookRiver(matrix, x, y - 1)
        return 1 + result
    else:
        return 0


