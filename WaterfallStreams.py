# 1st solution
# O(mn) time | O(mn) space
def waterfallStreams(array, source):
    dp = [[0 for _ in range(len(array[0]) + 2)] for _ in range(len(array))]
    waterFall = [[1] + line + [1] for line in array]
    dp[0][source + 1] = 100
    for i in range(len(dp) - 1):
        for j in range(1, len(dp[0]) - 1):
            if dp[i][j] != 0:
                if waterFall[i + 1][j] == 1:
                    left = j
                    while left > 0 and waterFall[i + 1][left] == 1 and waterFall[i][left - 1] == 0:
                        left -= 1
                    if waterFall[i + 1][left] == 0:
                        dp[i + 1][left] += dp[i][j] / 2.0
                    right = j
                    while right < len(waterFall[0]) - 1 and waterFall[i + 1][right] == 1 and waterFall[i][right + 1] == 0:
                        right += 1
                    if waterFall[i + 1][right] == 0:
                        dp[i + 1][right] += dp[i][j] / 2.0
                else:
                    dp[i + 1][j] += dp[i][j]
    return dp[-1][1:-1]