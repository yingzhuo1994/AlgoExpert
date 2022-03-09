# 1st solution
# O(w * h) time | O(w) space
# where w and h are the width and height of the matrix, respectively
def repeatedMatrixValues(matrix):
    answerSet = set(matrix[0])
    for i in range(1, len(matrix)):
        curRowSet = set(matrix[i])
        answerSet = answerSet.intersection(curRowSet)

    for j in range(len(matrix[0])):
        curColSet = set()
        for i in range(len(matrix)):
            curColSet.add(matrix[i][j])
        answerSet = answerSet.intersection(curColSet)
    return list(answerSet)
