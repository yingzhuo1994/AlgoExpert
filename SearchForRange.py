# 1st solution
# O(n) time | O(h) space
def searchForRange(array, target):
    left = binaryLeft(array, target)
    right = binaryRight(array, target)
    return [left, right] if array[left] <= target <= array[right] else [-1, -1]

def binaryLeft(array, target):
    left, right = 0, len(array) - 1
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def binaryRight(array, target):
    left, right = 0, len(array) - 1
    while left < right:
        mid = left + (right - left + 1) // 2
        if array[mid] <= target:
            left = mid
        else:
            right = mid - 1
    return left
