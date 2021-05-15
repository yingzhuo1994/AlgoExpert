def selectionSort(array):
    # Write your code here.
    for i in range(len(array) - 1):
        idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[idx]:
                idx = j
        array[i], array[idx] = array[idx], array[i]
    return array
