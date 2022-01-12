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
