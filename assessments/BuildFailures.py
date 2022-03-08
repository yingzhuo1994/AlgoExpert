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

# 2nd solution
# O(n * log(m)) time | O(n + log(m)) space
# where n is the number of build runs
# and m is the length of the longest build run
def buildFailures(buildRuns):
    greenPercentages = list(map(calculateGreenPercentage, buildRuns))
    return getLongestDecreasingSubarrayLength(greenPercentages)

def calculateGreenPercentage(buildRun):
    firstFalseIdx = binarySearchForFirstFalse(buildRun, 0, len(buildRun) - 1)
    return firstFalseIdx / len(buildRun)

# Recursive Binary Search
def binarySearchForFirstFalse(array, leftIdx, rightIdx):
    if leftIdx > rightIdx:
        return -1
    
    middleIdx = (leftIdx + rightIdx) // 2
    isFalse = not array[middleIdx]
    if isFalse:
        isFirstFalse = middleIdx == 0 or array[middleIdx - 1]
        if isFirstFalse:
            return middleIdx
        else:
            return binarySearchForFirstFalse(array, leftIdx, middleIdx - 1)
    else:
        return binarySearchForFirstFalse(array, middleIdx + 1, rightIdx)

def getLongestDecreasingSubarrayLength(array):
    longestLength = 1
    currentLongestLength = 1

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            currentLongestLength += 1
            longestLength = max(longestLength, currentLongestLength)
        else:
            currentLongestLength = 1
    
    return longestLength if longestLength > 1 else -1

# 3rd solution
# O(n * log(m)) time | O(1) space
# where n is the number of build runs
# and m is the length of the longest build run
def buildFailures(buildRuns):
    longestLength = 1
    currentLongestLength = 1
    previousGreenPercentage = calculateGreenPercentage(buildRuns[0])

    for i in range(1, len(buildRuns)):
        currentGreenPercentage = calculateGreenPercentage(buildRuns[i])
        if currentGreenPercentage < previousGreenPercentage:
            currentLongestLength += 1
            longestLength = max(longestLength, currentLongestLength)
        else:
            currentLongestLength = 1
        previousGreenPercentage = currentGreenPercentage
    
    return longestLength if longestLength > 1 else -1

def calculateGreenPercentage(buildRun):
    firstFalseIdx = binarySearchForFirstFalse(buildRun)
    return firstFalseIdx / len(buildRun)

# Iterative Binary Search
def binarySearchForFirstFalse(array):
    leftIdx = 0
    rightIdx = len(array) - 1

    while leftIdx <= rightIdx:
        middleIdx = (leftIdx + rightIdx) // 2
        isFalse = not array[middleIdx]
        if isFalse:
            isFirstFalse = middleIdx == 0 or array[middleIdx - 1]
            if isFirstFalse:
                return middleIdx
            else:
                rightIdx = middleIdx - 1
        else:
            leftIdx = middleIdx + 1

    return -1