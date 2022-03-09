# 1st solution
# O(w * h) time | O(w) space
# where w and h are the width and height of the matrix, respectively
def repeatedMatrixValues(matrix):
    answerSet = set(matrix[0])
    for i in range(1, len(matrix)):
        curRowSet = set()
        for j in range(len(matrix[0])):
            value = matrix[i][j]
            if value in answerSet:
                curRowSet.add(value)
        answerSet = curRowSet

    for j in range(len(matrix[0])):
        curColSet = set()
        for i in range(len(matrix)):
            value = matrix[i][j]
            if value in answerSet:
                curColSet.add(value)
        answerSet = curColSet
    return list(answerSet)

# 2nd solution
# O(w * h) time | O(min(w, h)) space
# where w and h are the width and height of the matrix, respectively
def repeatedMatrixValues(matrix):
    valueCounts = initializeCountsOfPotentialValues(matrix)

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            value = matrix[row][col]
            correctCountSoFar = row
            checkAndIncrementValueCount(value, valueCounts, correctCountSoFar)
    
    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            value = matrix[row][col]
            correctCountSoFar = len(matrix) + col
            checkAndIncrementValueCount(value, valueCounts, correctCountSoFar)
    
    finalValues = []
    for value in valueCounts:
        if valueCounts[value] == len(matrix) + len(matrix[0]):
            finalValues.append(value)
    
    return finalValues

def initializeCountsOfPotentialValues(matrix):
    valueCounts = {}

    smallerSide = matrix[0]
    if len(matrix) < len(matrix[0]):
        smallerSide = map(lambda row: row[0], matrix)
    
    for value in smallerSide:
        valueCounts[value] = 0
    
    return valueCounts

def checkAndIncrementValueCount(value, valueCounts, correctCountSoFar):
    if value not in valueCounts:
        return
    if valueCounts[value] != correctCountSoFar:
        return
    
    valueCounts[value] += 1
