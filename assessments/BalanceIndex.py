# 1st solution
# O(n) time | O(n) space
def balanceIndex(array):
    frontSumDic = {}
    total = 0
    for i in range(len(array)):
        frontSumDic[i] = total
        total += array[i]
    
    backSumDic = {}
    total = 0
    for i in reversed(range(len(array))):
        backSumDic[i] = total
        total += array[i]
    
    for i in range(len(array)):
        if frontSumDic[i] == backSumDic[i]:
            return i
    return -1

# 2nd solution
# O(n) time | O(1) space
# where n is the length of the input array
def balanceIndex(array):
    arraySum = sum(array)

    leftSideSum = 0
    rightSideSum = arraySum
    for i in range(len(array)):
        rightSideSum -= array[i]
        if leftSideSum == rightSideSum:
            return i
        leftSideSum += array[i]

    return -1

# 3rd solution
# O(n) time | O(n) space
# where n is the length of the input array
def balanceIndex(array):
    leftSideSums = array[:]

    leftSideSum = 0
    for i in range(len(array)):
        leftSideSums[i] = leftSideSum
        leftSideSum += array[i]
    
    rightSideSum = 0
    for i in reversed(range(len(array))):
        if leftSideSums[i] == rightSideSum:
            return i
        rightSideSum += array[i]
    
    return -1