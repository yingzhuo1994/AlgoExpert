def isMonotonic(array):
    # Write your code here.
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
