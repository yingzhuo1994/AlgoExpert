# 1st solution
# O(log(n)) time | O(1) space
def indexEqualsValue(array):
    ans = float("inf")
    left, right = 0, len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] > mid:
            right = mid -1
        elif array[mid] < mid:
            left = mid + 1
        else:
            ans = min(ans, mid)
            right = mid - 1
    return ans if ans != float('inf') else -1

# 2nd solution
# O(log(n)) time | O(1) space
def indexEqualsValue(array):
    leftIndex = 0
    rightIndex = len(array) - 1

    while leftIndex <= rightIndex:
        middleIndex = leftIndex + (rightIndex - leftIndex) // 2
        middleValue = array[middleIndex]

        if middleValue < middleIndex:
            leftIndex = middleIndex + 1
        elif middleValue == middleIndex and middleIndex == 0:
            return middleIndex
        elif middleValue == middleIndex and array[middleIndex - 1] < middleIndex - 1:
            return middleIndex
        else:
            rightIndex = middleIndex - 1
    
    return -1