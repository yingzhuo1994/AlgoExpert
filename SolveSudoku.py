# 1st solution
# O(1) time | O(1) space
def solveSudoku(board):
    stack = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                stack.append((i, j))
    dfs(board, stack, 0)
    return board

def dfs(board, stack, idx):
    if idx == len(stack):
        return True
    x, y = stack[idx]
    for num in range(1, 10):
        if check(num, board, x, y):
            board[x][y] = num
            if dfs(board, stack, idx + 1):
                return True
        board[x][y] = 0
    return False
        
def check(value, board, i, j):
    for x in range(len(board)):
        if board[x][j] == value:
            return False

    for y in range(len(board[0])):
        if board[i][y] == value:
            return False
    
    gridRow = i // 3
    gridCol = j // 3

    for x in range(gridRow * 3, (gridRow + 1) * 3):
        for y in range(gridCol * 3, (gridCol + 1) * 3):
            if board[x][y] == value:
                return False
    
    return True

# 2nd solution
# O(1) time | O(1) space
def solveSudoku(board):
    solvePartialSudoku(0, 0, board)
    return board

def solvePartialSudoku(row, col, board):
    currentRow = row
    currentCol = col

    if currentCol == len(board[currentRow]):
        currentRow += 1
        currentCol = 0
        if currentRow == len(board):
            return True # board is completed
    
    if board[currentRow][currentCol] == 0:
        return tryDigitsAtPosition(currentRow, currentCol, board)
    
    return solvePartialSudoku(currentRow, currentCol + 1, board)

def tryDigitsAtPosition(row, col, board):
    for digit in range(1, 10):
        if isValidAtPosition(digit, row, col, board):
            board[row][col] = digit
            if solvePartialSudoku(row, col + 1, board):
                return True
    board[row][col] = 0
    return False

def isValidAtPosition(value, row, col, board):
    rowIsValid = value not in board[row]
    columnIsValid = value not in map(lambda r: r[col], board)

    if not rowIsValid or not columnIsValid:
        return False
    
    # Check subgrid constraint
    subgridRowStart = (row // 3) * 3
    subgridColStart = (col // 3) * 3
    for rowIdx in range(3):
        for colIdx in range(3):
            rowToCheck = subgridRowStart + rowIdx
            colToCheck = subgridColStart + colIdx
            existingValue = board[rowToCheck][colToCheck]

            if existingValue == value:
                return False
    
    return True