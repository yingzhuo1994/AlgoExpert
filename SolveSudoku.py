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
        board[x][y] = num
        if check(board, x, y):
            if dfs(board, stack, idx + 1):
                return True
        board[x][y] = 0
    return False
        
def check(board, i, j):
    test = board[i][j]
    for x in range(len(board)):
        if x != i and board[x][j] == test:
            return False

    for y in range(len(board[0])):
        if y != j and board[i][y] == test:
            return False
    
    gridRow = i // 3
    gridCol = j // 3

    for x in range(gridRow * 3, (gridRow + 1) * 3):
        for y in range(gridCol * 3, (gridCol + 1) * 3):
            if (x, y) != (i, j) and board[x][y] == test:
                return False
    
    return True



    