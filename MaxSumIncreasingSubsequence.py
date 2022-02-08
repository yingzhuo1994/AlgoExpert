# 1st solution, my solution
# O(n^2) time | O(n) space
def maxSumIncreasingSubsequence(array):
    # Write your code here.
    table = [[i, array[i]] for i in range(len(array))]
    for i in range(len(array)):
        maxBeforeIndex = -1
        maxBeforeValue = float('-inf')
        for j in range(i):
            if array[j] < array[i] and table[j][1] > maxBeforeValue:
                maxBeforeIndex = j
                maxBeforeValue = table[j][1]
        if maxBeforeIndex != -1 and maxBeforeValue > 0:
            table[i][0] = maxBeforeIndex
            table[i][1] += maxBeforeValue
    print(table)
    nextIdx, maxSum = max(table, key = lambda lst: lst[1])

    start = table.index([nextIdx, maxSum])
    lst = [array[start]]
    while start != nextIdx:
        start = nextIdx
        lst.append(array[start])
        nextIdx = table[start][0]
    return [maxSum, lst[::-1]]

# 2nd solution, official solution
# O(n^2) time | O(n) space
def maxSumIncreasingSubsequence(array):
    sequences = [None for _ in array]
    sums = [num for num in array]
    maxSumIdx = 0
    for i in range(len(array)):
        currentNum = array[i]
        for j in range(0, i):
            otherNum = array[j]
            if otherNum < currentNum and sums[j] + currentNum > sums[i]:
                sums[i] = sums[j] + currentNum
                sequences[i] = j
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i
    return [sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)]

def buildSequence(array, sequences, currentIdx):
    result = []
    while currentIdx is not None:
        result.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(result))