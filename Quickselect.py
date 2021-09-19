def quickselect(array, k):
    pivot = array[0]
    left = [num for num in array if num < pivot]
    middle = [num for num in array if num == pivot]
    right = [num for num in array if num > pivot]
    L = len(left)
    M = len(middle)
    if k <= L:
        return quickselect(left, k)
    elif k > L + M:
        return quickselect(right, k - L - M)
    else:
        return middle[0]

# 2nd solution
def quickselect(array, k):
    position = k - 1
    return quickselectHelper(array, 0, len(array) - 1, position)

def quickselectHelper(array, startIdx, endIdx, position):
    while True:
        if startIdx > endIdx:
            raise Exception("Your algorithm should never arrive here!")
        pivotIdx = startIdx
        leftIdx = startIdx + 1
        rightIdx = endIdx
        while leftIdx <= rightIdx:
            if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
                swap(array, leftIdx, rightIdx)
            if array[leftIdx] <= array[pivotIdx]:
                leftIdx += 1
            if array[rightIdx] >= array[pivotIdx]:
                rightIdx -= 1
        swap(array, pivotIdx, rightIdx)
        if rightIdx == position:
            return array[rightIdx]
        elif rightIdx < position:
            startIdx = rightIdx + 1
        else:
            endIdx = rightIdx - 1

def swap(array, one, two):
    array[one], array[two] = array[two], array[one]
