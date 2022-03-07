# 1st solution
# O(n^2) time | O(1) space
def spinRings(array):
    n = len(array)
    for k in range(n // 2):
        rotate(array, k)
    return array

def rotate(array, k):
    start = k
    end = len(array) - k
    tmp = array[start][start]
    for j in range(start + 1, end):
        array[start][j], tmp = tmp, array[start][j]
    
    for i in range(start + 1, end):
        array[i][end-1], tmp = tmp, array[i][end-1]
    
    for j in reversed(range(start, end - 1)):
        array[end-1][j], tmp = tmp, array[end-1][j]
    
    for i in reversed(range(start, end - 1)):
        array[i][start], tmp = tmp, array[i][start]

# 2nd solution
# O(n^2) time | O(n) space
# where n is the size of the array
def spinRings(array):
    spinRingsHelper(array, 0, len(array) - 1, 0, len(array) - 1)

def spinRingsHelper(array, startRow, endRow, startCol, endCol):
    if startRow >= endRow and startCol >= endCol:
        return 
    
    originalTopRightValue = array[startRow][endCol]

    for col in reversed(range(startCol + 1, endCol + 1)):
        array[startRow][col] = array[startRow][col - 1]
    
    for row in range(startRow, endRow):
        array[row][startCol] = array[row + 1][startCol]
    
    for col in range(startCol, endCol):
        array[endRow][col] = array[endRow][col + 1]
    
    for row in reversed(range(startRow + 2, endRow + 1)):
        array[row][endCol] = array[row - 1][endCol]
    
    array[startRow + 1][endCol] = originalTopRightValue

    spinRingsHelper(array, startRow + 1, endRow - 1, startCol + 1, endCol - 1)

# 3rd solution
# O(n^2) time | O(1) space
# where n is the size of the array
def spinRings(array):
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array) - 1

    while startRow < endRow and startCol < endCol:
        originalTopRightValue = array[startRow][endCol]

        for col in reversed(range(startCol + 1, endCol + 1)):
            array[startRow][col] = array[startRow][col - 1]
        
        for row in range(startRow, endRow):
            array[row][startCol] = array[row + 1][startCol]
        
        for col in range(startCol, endCol):
            array[endRow][col] = array[endRow][col + 1]
        
        for row in reversed(range(startRow + 2, endRow + 1)):
            array[row][endCol] = array[row - 1][endCol]
        
        array[startRow + 1][endCol] = originalTopRightValue

        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1