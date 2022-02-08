# 1st recursive solution
# O(2^n) time | O(n) space
def maxSubsetSumNoAdjacent(array):
    if not array:
        return 0
    if len(array) == 1:
        return array[0]
    withFirst = array[0] + maxSubsetSumNoAdjacent(array[2:])
    withoutFirst = maxSubsetSumNoAdjacent(array[1:])
    return max(withFirst, withoutFirst)

# 2nd iterative solution
# O(n) time | O(n) space
def maxSubsetSumNoAdjacent(array):
    if not array:
        return 0
    elif len(array) == 1:
        return array[0]
    maxSums = array[:]
    maxSums[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSums[i] = max(maxSums[i - 1], maxSums[i - 2] + array[i])
    return maxSums[-1]

# 3rd iterative solution
# O(n) time | O(1) space
def maxSubsetSumNoAdjacent(array):
    if not array:
        return 0
    elif len(array) == 1:
        return array[0]
    second = array[0]
    first = max(array[0], array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        first, second = current, first
    return first
