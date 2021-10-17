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
                largestLength = max(largestLength, dp[i][1])
        if dp[i][1] >= largestLength:
            largestIdx = i
	result = []
	idx = largestIdx
    while idx is not None:
        result.append(array[idx])
        idx = dp[idx][0]
    return result[::-1]