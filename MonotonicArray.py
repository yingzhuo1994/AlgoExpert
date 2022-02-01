# 1st solution
# O(n) time | O(1) space
def isMonotonic(array):
    mode = 0
    for i in range(len(array) - 1):
        if array[i + 1] > array[i]:
            if mode < 0:
                return False
            else:
                mode = 1
        elif array[i + 1] < array[i]:
            if mode > 0:
                return False
            else:
                mode = -1
    return True

# 2nd solution
# O(n) time | O(1) space
def isMonotonic(array):
    if len(array) <= 2:
        return True
    
    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i - 1]
        if breaksDirection(direction, array[i - 1], array[i]):
            return False
    
    return True

def breaksDirection(direction, previousInt, currentInt):
    difference = currentInt - previousInt
    if direction > 0:
        return difference < 0
    return difference > 0

# 3rd solution
# O(n) time | O(1) space
def isMonotonic(array):
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isNonDecreasing = False
        if array[i] > array[i - 1]:
            isNonIncreasing = False
    
    return isNonDecreasing or isNonIncreasing