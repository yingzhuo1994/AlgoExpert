# 1st solution
# O(n) time | O(n) space
# where n is the total number of elements in the matrix
def longestIncreasingMatrixPath(matrix):
    dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    longestLength = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            dfs(matrix, dp, i, j)
            longestLength = max(longestLength, dp[i][j])
    return longestLength

def dfs(matrix, dp, i, j):
    if dp[i][j] > 0:
        return 
    neighbors = getNeighbors(matrix, i, j)
    value = matrix[i][j]
    longestLength = 1
    for row, col in neighbors:
        if matrix[row][col] > value:
            dfs(matrix, dp, row, col)
            longestLength = max(longestLength, dp[row][col] + 1)
    dp[i][j] = longestLength

def getNeighbors(matrix, i, j):
    neighbors = []
    for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        row = i + dx
        col = j + dy
        if 0 <= row and row < len(matrix) and 0 <= col and col < len(matrix[0]):
            neighbors.append([row, col])
    return neighbors

# 2nd solution
# O(n) time | O(n) space
# where n is the total number of elements in the matrix
def longestIncreasingMatrixPath(matrix):
    longestPathLengths = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix[0])):
            row.append(None)
        longestPathLengths.append(row)
    
    longestPathLength = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            longestPathLength = max(
                getLongestPathLengthAt(matrix, row, col, float("-inf"), longestPathLengths),
                longestPathLength,
            )
    
    return longestPathLength

def getLongestPathLengthAt(matrix, row, col, lastPathValue, longestPathLengths):
    isOutOfBounds = row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0])
    if isOutOfBounds:
        return 0
    
    currentValue = matrix[row][col]
    if currentValue <= lastPathValue:
        return 0
    
    if longestPathLengths[row][col] is None:
        longestPathLengths[row][col] = 1 + max(
            getLongestPathLengthAt(matrix, row - 1, col, currentValue, longestPathLengths),
            getLongestPathLengthAt(matrix, row + 1, col, currentValue, longestPathLengths),
            getLongestPathLengthAt(matrix, row, col - 1, currentValue, longestPathLengths),
            getLongestPathLengthAt(matrix, row, col + 1, currentValue, longestPathLengths)
        )
    
    return longestPathLengths[row][col]