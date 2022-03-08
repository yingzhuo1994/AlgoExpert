# 1st solution
# O(n * log(m)) time | O(1) space
# where n is the number of build runs
# and m is the length of the longest build run
def buildFailures(buildRuns):
    greatestDecreasingNumber = 0
    currentDecreasingNumber = 0
    lastGreenRate = 2
    for run in buildRuns:
        currentGreenRate = calculateGreenPercentage(run)
        if currentGreenRate < lastGreenRate:
            currentDecreasingNumber += 1
        else:
            currentDecreasingNumber = 1
        lastGreenRate = currentGreenRate
        greatestDecreasingNumber = max(greatestDecreasingNumber, currentDecreasingNumber)
    return greatestDecreasingNumber if greatestDecreasingNumber != 1 else -1

def calculateGreenPercentage(run):
    left, right = 0, len(run)
    while left < right:
        middle = left + (right - left) // 2
        if run[middle]:
            left = middle + 1
        else:
            right = middle
    return left / len(run)