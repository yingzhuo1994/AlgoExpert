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
def balanceIndex(array):
    totalSum = sum(array)
    frontSum = 0
    for i in range(len(array)):
        backSum = totalSum - frontSum - array[i]
        if frontSum == backSum:
            return i
        frontSum += array[i]
    return -1