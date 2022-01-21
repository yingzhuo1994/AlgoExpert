# 1st solution
def rightSmallerThan(array):
    ans = [0 for _ in array]
    arr = [[array[i], i] for i in range(len(array))]
    mergeSort(arr, ans)
    return ans

def mergeSort(array, ans):
    if len(array) <= 1:
        return array
    half = len(array) // 2
    left = mergeSort(array[:half], ans)
    right = mergeSort(array[half:], ans)
    newArray = []
    for i in range(len(left)):
        for j in range(len(right)):
            if left[i][0] > right[j][0]:
                ans[left[i][1]] += 1

    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            newArray.append(left[i])
            i += 1
        else:
            newArray.append(right[j])
            j += 1
    newArray.extend(left[i:] or right[j:])
    return newArray    
    
