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