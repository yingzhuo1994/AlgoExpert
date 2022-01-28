# 1st solution
def nonAttackingQueens(n):
    table = [[0 for _ in range(n)] for _ in range(n)]
    ans = [0]
    for i in range(n):
        dfs(table, 0, i, n, ans)
    return ans[0]

def dfs(table, i, j, queens, ans):
    if table[i][j] == 1:
        return
    table[i][j] = 1
    if checkTable(table, i, j):
        queens -= 1
        if queens == 0:
            ans[0] += 1
        else:   
            for col in range(len(table)):
                dfs(table, i + 1, col, queens, ans)
    table[i][j] = 0

def checkTable(table, i, j):
    for row in range(len(table)):
        if row != i and table[row][j] == 1:
            return False
    for col in range(len(table)):
        if col != j and table[i][col] == 1:
            return False
    for row in range(len(table)):
        col = i - row + j
        if row != i and 0 <= col < len(table) and table[row][col] == 1:
            return False
    for row in range(len(table)):
        col = row - i + j
        if row != i and 0 <= col < len(table) and table[row][col] == 1:
            return False
    return True

# 2nd solution
# Lower Bound: O(n!) time | O(n) space - where n is the input number
def nonAttackingQueens(n):
    # Each index of `columnPlacements` represents a row of the chessboard,
    # and the value at each index is the column (on the relevant row) where
    # a queen is currently placed.
    columnPlacements = [0] * n
    return getNumberOfNonAttackingQueenPlacements(0, columnPlacements, n)

def getNumberOfNonAttackingQueenPlacements(row, columnPlacements, boardSize):
    if row == boardSize:
        return 1
    
    validPlacements = 0
    for col in range(boardSize):
        if isNonAttackingPlacement(row, col, columnPlacements):
            columnPlacements[row] = col
            validPlacements += getNumberOfNonAttackingQueenPlacements(row + 1, columnPlacements, boardSize)
    
    return validPlacements

# As `row` tends to `n`, this becomes an O(n)-time operation.
def isNonAttackingPlacement(row, col, columnPlacements):
    for previousRow in range(row):
        columnToCheck = columnPlacements[previousRow]
        sameColumn = columnToCheck == col
        onDiagonal = abs(columnToCheck - col) == row - previousRow
        if sameColumn or onDiagonal:
            return False
    return True