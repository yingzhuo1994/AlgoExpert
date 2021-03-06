# 1st solution
# O(n) time | O(1) space
def threeNumberSort(array, order):
    # Write your code here.
    start = 0
    end = len(array) - 1
    i = 0
    while i <= end:
        if array[i] == order[0]:
            array[i], array[start] = array[start], array[i]
            i += 1
            start += 1
        elif array[i] == order[2]:
            array[i], array[end] = array[end], array[i]
            end -= 1
        else:
            i += 1
    return array

# 2nd solution
# O(n) time | O(1) space
def threeNumberSort(array, order):
    valueCounts = [0, 0, 0]

    for element in array:
        orderIdx = order.index(element)
        valueCounts[orderIdx] += 1
    
    for i in range(3):
        value = order[i]
        count = valueCounts[i]

        numElementsBefore = sum(valueCounts[:i])
        for n in range(count):
            currentIdx = numElementsBefore + n
            array[currentIdx] = value
    
    return array

# 3rd solution
# O(n) time | O(1) space
def threeNumberSort(array, order):
    firstValue = order[0]
    thirdValue = order[2]

    firstIdx = 0
    for idx in range(len(array)):
        if array[idx] == firstValue:
            array[firstIdx], array[idx] = array[idx], array[firstIdx]
            firstIdx += 1
    
    thirdIdx = len(array) - 1
    for idx in range(len(array) - 1, - 1, -1):
        if array[idx] == thirdValue:
            array[thirdIdx], array[idx] = array[idx], array[thirdIdx]
            thirdIdx -= 1
        
    return array