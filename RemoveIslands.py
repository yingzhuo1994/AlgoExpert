def removeIslands(matrix):
    # Write your code here.
    for j in range(len(matrix[0])):
        findLand(matrix, 0, j)
        findLand(matrix, len(matrix) - 1, j)
    for i in range(1, len(matrix) - 1):
        findLand(matrix, i, 0)
        findLand(matrix, i, len(matrix[0]) - 1)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'X':
                matrix[i][j] = 1
            else:
                matrix[i][j] = 0
	return matrix

def findLand(matrix, i, j):
    if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and matrix[i][j] == 1:
        matrix[i][j] = 'X'
        findLand(matrix, i + 1, j)
        findLand(matrix, i - 1, j)
        findLand(matrix, i, j + 1)
        findLand(matrix, i, j - 1)
