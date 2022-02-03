# 1st solution
# O(n) time | O(n) space
def firstDuplicateValue(array):
    dic = {}
    for elem in array:
        if elem in dic:
            return elem
        else:
            dic[elem] = 1
    return -1

# 2nd solution
# O(n) time | O(n) space
def firstDuplicateValue(array):
    for i in range(len(array)):
        if array[i] in array[:i]:
            return array[i]
    return -1

# 3rd solution
# O(n) time | O(1) space
def firstDuplicateValue(array):
    for i in range(len(array)):
        num = abs(array[i])
        index = num - 1
        if array[index] < 0:
            return num
        array[index] *= -1
    return -1
