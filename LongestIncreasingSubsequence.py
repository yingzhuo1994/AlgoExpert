# 1st solution
# O(n^2) time | O(n) space
from LongestCommonSubsequence import buildSequence


def longestIncreasingSubsequence(array):
    dp = [[None, 1] for i in array]
    largestIdx = 0
    largestLength = 0
    for i in range(len(array)):
        for j in range(i):
            if array[j] < array[i] and dp[j][1]  + 1 > dp[i][1]:
                dp[i] = [j, dp[j][1] + 1]
                largestLength = max(largestLength, dp[i][1])
        if dp[i][1] >= largestLength:
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