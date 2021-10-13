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
# O(w * h) time | O(w * h) space
# where w is the width of the matrix and h is the height
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

# 3rd solution, official dp solution
# O(w * h) time | O(w * h) space
# where w is the width of the matrix and h is the height
def maximumSumSubmatrix(matrix, size):
    sums = createSumMatrix(matrix)
    maxSubMatrixSum = float("-inf")

    for row in range(size - 1, len(matrix)):
        for col in range(size - 1, len(matrix[row])):
            total = sums[row][col]

            touchesTopBorder = row - size < 0
            if not touchesTopBorder:
                total -= sums[row - size][col]
            
            touchesLeftBorder = col - size < 0
            if not touchesLeftBorder:
                total -= sums[row][col - size]
            
            touchesTopOrLeftBorder = touchesTopBorder or touchesLeftBorder
            if not touchesTopOrLeftBorder:
                total += sums[row - size][col - size]
            
            maxSubMatrixSum = max(maxSubMatrixSum, total)
    
    return maxSubMatrixSum

def createSumMatrix(matrix):
    sums = [[0 for _ in range(len(matrix[row]))] for row in range(len(matrix))]
    sums[0][0] = matrix[0][0]

    # Fill the first Row.
    for idx in range(1, len(matrix[0])):
        sums[0][idx] = sums[0][idx - 1] + matrix[0][idx]
    
    # Fill the first column.
    for idx in range(1, len(matrix)):
        sums[idx][0] = sums[idx - 1][0] + matrix[idx][0]
    
    # Fill the rest of the matrix.
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[row])):
            sums[row][col] = sums[row - 1][col] + sums[row][col - 1] - sums[row - 1][col - 1] + matrix[row][col]
    
    return sums