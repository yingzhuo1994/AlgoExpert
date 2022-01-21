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

# 2nd solution
# O(w^2 * h) time | O(w) space - where w and h
# are the width and height of the input array
def waterfallStreams(array, source):
    rowAbove =array[0][:]
    # We'll use -1 to represent water, since 1 is used for a block.
    rowAbove[source] = -1

    for row in range(1, len(array)):
        currentRow = array[row][:]

        for idx in range(len(rowAbove)):
            valueAbove = rowAbove[idx]

            hasWaterAbove = valueAbove < 0
            hasBlock = currentRow[idx] == 1

            if not hasWaterAbove:
                continue

            if not hasBlock:
                # If there is no block in the current column, move the water down.
                currentRow[idx] += valueAbove
                continue

            splitWater = valueAbove / 2

            # Move water right.
            rightIdx = idx
            while rightIdx + 1 < len(rowAbove):
                rightIdx += 1
                if rowAbove[rightIdx] == 1: # if there is a block in the way
                    break
                if currentRow[rightIdx] != 1: # if there is no block below us
                    currentRow[rightIdx] += splitWater
                    break
            
            # Move water left.
            leftIdx = idx
            while leftIdx - 1 >= 0:
                leftIdx -= 1
                if rowAbove[leftIdx] == 1: # if there is a block in the way
                    break
                if currentRow[leftIdx] != 1: # if there is no block below us
                    currentRow[leftIdx] += splitWater
                    break
        
        rowAbove = currentRow
    
    # Convert our negative values to positive percentages.
    finalPercentages = list(map(lambda num: num * (-100), rowAbove))

    return finalPercentages