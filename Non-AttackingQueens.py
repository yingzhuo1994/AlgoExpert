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

def printTable(table):
    for line in table:
        print(line)