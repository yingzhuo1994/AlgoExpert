# 1st solution
# O(mn) time | O(n) space
def numberOfWaysToTraverseGraph(width, height):
    steps = [1 for _ in range(width)]
    for i in range(height - 1):
        for j in reversed(range(width - 1)):
            steps[j] = steps[j] + steps[j + 1]
    return steps[0]

# 2nd solution
# O(m + n) time | O(1) space
def numberOfWaysToTraverseGraph(width, height):
    m = width - 1
    n = height - 1
    numerator = factorial(m + n)
    denominator = factorial(m) * factorial(n)
    return numerator // denominator

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result