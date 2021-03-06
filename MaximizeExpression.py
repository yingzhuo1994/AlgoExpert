# 1st solution, brute force
# O(n^4) time | O(1) space
def maximizeExpression(array):
    if len(array) < 4:
        return 0
    maxResult = float('-inf')
    for a in range(len(array) - 3):
        for b in range(a + 1, len(array) - 2):
            for c in range(b + 1, len(array) - 1):
                for d in range(c + 1, len(array)):
                    maxResult = max(maxResult, expression(array, a, b, c, d))
    return maxResult
                    
def expression(array, a, b, c, d):
    return array[a] - array[b] + array[c] - array[d]


# 2nd solution, dynamic programming
# O(n) time | O(n) space
def maximizeExpression(array):
    if len(array) < 4:
        return 0
    
    n = len(array)
    maxOfA = [array[0]]
    maxOfAMinusB = [float("-inf")]
    maxOfAMinusBPlusC = [float("-inf")] * 2
    maxOfAMinusBPlusCMinusD = [float("-inf")] * 3

    for idx in range(1, n):
        currentMax = max(maxOfA[idx - 1], array[idx])
        maxOfA.append(currentMax)
    
    for idx in range(1, n):
        currentMax = max(maxOfAMinusB[idx - 1], maxOfA[idx -1] - array[idx])
        maxOfAMinusB.append(currentMax)

    for idx in range(2, n):
        currentMax = max(maxOfAMinusBPlusC[idx - 1], maxOfAMinusB[idx - 1] + array[idx])
        maxOfAMinusBPlusC.append(currentMax)
    
    for idx in range(3, n):
        currentMax = max(maxOfAMinusBPlusCMinusD[idx - 1], maxOfAMinusBPlusC[idx - 1] - array[idx])
        maxOfAMinusBPlusCMinusD.append(currentMax)

    return maxOfAMinusBPlusCMinusD[-1]


# 3rd solution, dynamic programming
# O(n) time | O(n) space
def maximizeExpression(array):
    if len(array) < 4:
        return 0
    
    n = len(array) - 3
    lst = []

    curMax = float("-inf")
    for idx in range(n):
        curMax = max(curMax, array[idx])
        lst.append(curMax)
    
    curMax = float("-inf")
    for idx in range(n):
        b = idx + 1
        curMax = max(curMax, lst[idx] - array[b])
        lst[idx] = curMax

    curMax = float("-inf")
    for idx in range(n):
        c = idx + 2
        curMax = max(curMax, lst[idx] + array[c])
        lst[idx] = curMax

    curMax = float("-inf")  
    for idx in range(n):
        d = idx + 3
        curMax = max(curMax, lst[idx] - array[d])
        lst[idx] = curMax

    return lst[-1]