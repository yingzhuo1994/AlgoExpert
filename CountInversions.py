# 1st solution
# O(n*log(n)) time | O(n*log(n)) space
def countInversions(array):
    ans = [0]
    mergeSort(array, ans)
    return ans[0]

def mergeSort(array, ans):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = mergeSort(array[:mid], ans)
    right = mergeSort(array[mid:], ans)
    newArray = []
    for num in left:
        ans[0] += binarySearch(right, num)
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            newArray.append(left[i])
            i += 1
        else:
            newArray.append(right[j])
            j += 1

    newArray.extend(left[i:] or right[j:])
    return newArray

def binarySearch(array, num):
    left, right = 0, len(array)
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] < num:
            left = mid + 1
        else:
            right = mid
    return left