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