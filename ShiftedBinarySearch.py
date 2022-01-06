def shiftedBinarySearch(array, target):
    left, right = 0, len(array) - 1
    while left < right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid
        if array[left] < array[right]:
            if array[mid] < target:
                left = mid + 1
            else:
                right = mid
        else:
            if array[left] < array[mid]:
                if array[left] <= target < array[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if array[mid] < target <= array[right]:
                    left = mid + 1
                else:
                    right = mid
    return left if array[left] == target else -1
                

