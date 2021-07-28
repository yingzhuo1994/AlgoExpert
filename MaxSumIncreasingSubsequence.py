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