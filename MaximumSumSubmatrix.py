# 1st brute force solution
def maximumSumSubmatrix(matrix, size):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0] * (n - size + 1)] * (m - size + 1)
    maxSum = float('-inf')
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            dp[i][j] = getSum(matrix, i, i + size - 1, j, j + size - 1)
            maxSum = max(maxSum, dp[i][j])
    return maxSum

def getSum(matrix, rowOne, rowTwo, colOne, colTwo):
    result = 0
    for i in range(rowOne, rowTwo + 1):
        for j in range(colOne, colTwo + 1):
            result += matrix[i][j]
    return result

# 2nd solution, dp
def maximumSumSubmatrix(matrix, size):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0] * (n - size + 1)] * (m - size + 1)
    dp[0][0] = getSum(matrix, 0, size - 1, 0, size - 1)
    maxSum = dp[0][0]
    for j in range(1, len(dp[0])):
        dp[0][j] = dp[0][j - 1] + getSum(matrix, 0, size - 1, j + size - 1, j + size - 1) - getSum(matrix, 0, size - 1, j - 1, j - 1)
        maxSum = max(maxSum, dp[0][j])

    for i in range(1, len(dp)):
        for j in range(len(dp[0])):
            dp[i][j] = dp[i -1][j] + getSum(matrix, i + size - 1, i + size - 1, j, j + size - 1) - getSum(matrix, i - 1, i - 1, j, j + size - 1)
            maxSum = max(maxSum, dp[i][j])
    return maxSum

def getSum(matrix, rowOne, rowTwo, colOne, colTwo):
    result = 0
    for i in range(rowOne, rowTwo + 1):
        for j in range(colOne, colTwo + 1):
            result += matrix[i][j]
    return result