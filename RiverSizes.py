# 1st solution
# O(wh) time | O(wh) space
def riverSizes(matrix):
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

# 2nd solution
# O(wh) time | O(wh) space
def riverSizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i, j, matrix, visited, sizes)
    return sizes

def traverseNode(i, j, matrix, visited, sizes):
    currentRiverSize = 0
    nodesToExplore = [[i, j]]
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentRiverSize += 1
        unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)

def getUnvisitedNeighbors(i, j, matrix, visited):
    unvisitedNeighbors = []
    for row, col in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
        if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and not visited[row][col]:
            unvisitedNeighbors.append([row, col])
    return unvisitedNeighbors