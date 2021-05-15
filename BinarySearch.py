def binarySearch(array, target):
    # Write your code here.
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1
