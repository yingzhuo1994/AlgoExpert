# 1st brute force solution
def maximumSumSubmatrix(matrix, size):
    # Write your code here.
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