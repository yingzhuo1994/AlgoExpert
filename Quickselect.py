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