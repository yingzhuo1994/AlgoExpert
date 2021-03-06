# 1st solution
# O(n^2) time | O(n) space
def longestIncreasingSubsequence(array):
    dp = [[None, 1] for i in array]
    largestIdx = 0
    largestLength = 0
    for i in range(len(array)):
        for j in range(i):
            if array[j] < array[i] and dp[j][1]  + 1 > dp[i][1]:
                dp[i] = [j, dp[j][1] + 1]
        if dp[i][1] >= largestLength:
            largestLength = dp[i][1]
            largestIdx = i
    result = []
    idx = largestIdx
    while idx is not None:
        result.append(array[idx])
        idx = dp[idx][0]
    return result[::-1]

# 2nd solution
# O(n^2) time | O(n) space
def longestIncreasingSubsequence(array):
    sequences = [None for x in array]
    lengths = [1 for x in array]
    maxLengthIdx = 0
    for i in range(len(array)):
        currentNum = array[i]
        for j in range(i):
            otherNum = array[j]
            if otherNum < currentNum and lengths[j] + 1 >= lengths[i]:
                lengths[i] = lengths[j] + 1
                sequences[i] = j
        if lengths[i] >= lengths[maxLengthIdx]:
            maxLengthIdx = i
    return buildSequence(array, sequences, maxLengthIdx)

def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))

# 3rd solution
# O(nlog(n)) time | O(n) space
def longestIncreasingSubsequence(array):
    sequences = [None for x in array]
    indices = [None for x in range(len(array) + 1)]
    length = 0
    for i, num in enumerate(array):
        newLength = binarySearch(1, length, indices, array, num)
        sequences[i] = indices[newLength - 1]
        indices[newLength] = i
        length = max(length, newLength)
    return buildSequence(array, sequences, indices[length])

def binarySearch(startIdx, endIdx, indices, array, num):
	while startIdx <= endIdx:
		idx = (startIdx + endIdx) // 2
		if array[indices[idx]] < num:
			startIdx = idx + 1
		else:
			endIdx = idx - 1
	return startIdx

def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))