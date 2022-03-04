# 1st solution
# O(n) time | O(n) space
def longestStreakOfAdjacentOnes(array):
    stack = []
    for i, num in enumerate(array):
        if num == 0:
            stack.append(i)
    
    possibleIdx = -1
    largestLength = 0
    for i, idx in enumerate(stack):
        if i == 0:
            front = idx
        else:
            front = idx - stack[i-1] - 1
        if i == len(stack) - 1:
            back = len(array) - idx - 1
        else:
            back = stack[i+1] - idx - 1
        length = front + 1 + back
        if length > largestLength:
            largestLength = length
            possibleIdx = idx
    return possibleIdx

# 2nd solution
# O(n) time | O(1) space
def longestStreakOfAdjacentOnes(array):
    possibleIdx = -1
    largestLength = 0
    frontIdx = -1
    frontLength = -1
    for i, num in enumerate(array):
        if num == 0:
            backLength = i - frontIdx - 1
            length = frontLength + backLength + 1
            if length > largestLength:
                largestLength = length
                possibleIdx = frontIdx
            frontLength = backLength
            frontIdx = i

    backLength = len(array) - frontIdx - 1
    length = frontLength + backLength + 1
    if length > largestLength:
        largestLength = length
        possibleIdx = frontIdx

    return possibleIdx

# 3rd solution
# O(n) time | O(1) space
def longestStreakOfAdjacentOnes(array):
    longestStreakLength = 0
    longestStreakReplacedZeroIdx = -1

    currentStreakLength = 0
    replacedZeroIdx = -1

    for i in range(len(array)):
        if array[i] == 1:
            currentStreakLength += 1
        else:
            currentStreakLength = i - replacedZeroIdx
            replacedZeroIdx = i
        
        if currentStreakLength > longestStreakLength:
            longestStreakLength = currentStreakLength
            longestStreakReplacedZeroIdx = replacedZeroIdx
    
    return longestStreakReplacedZeroIdx