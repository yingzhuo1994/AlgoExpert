def riverSizes(matrix):
    # Write your code here.
    lst = []
    lengthLst = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1 and (i, j) not in lst:
                length = lookRiver(matrix, i, j, lst)
                lengthLst.append(length)
    return lengthLst
    

def lookRiver(matrix, x, y, lst):
    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] == 1 and (x, y) not in lst:
        lst.append((x, y))
        result = lookRiver(matrix, x + 1, y, lst) + lookRiver(matrix, x - 1, y, lst)\
             + lookRiver(matrix, x, y + 1, lst) + lookRiver(matrix, x, y - 1, lst)
        return 1 + result
    else:
        return 0

