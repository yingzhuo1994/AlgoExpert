# 1st solution
# O(n^3) time | O(n^2) space
def squareOfZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[[0,0] for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                continue
            dp[i][j] = [1, 1]
            if i > 0:
                dp[i][j][0] += dp[i - 1][j][0]
            if j > 0:
                dp[i][j][1] += dp[i][j - 1][1]
    for i in range(m):
        for j in range(n):
            row, col = dp[i][j]
            if row == 0 or col == 0:
                continue
            size = min(row, col)
            for k in range(1, size):
                if min(dp[i-k][j][1], dp[i][j-k][0]) > k:
                    return True
    return False
