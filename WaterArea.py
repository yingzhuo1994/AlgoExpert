# 1st solution
# O(n) time | O(1) space
def waterArea(heights):
    left, right = 0, len(heights) - 1
    leftMax, rightMax = 0, 0
    totalWater = 0
    while left < right:
        if heights[left] < heights[right]:
            if heights[left] >= leftMax:
                leftMax = heights[left]
            else:
                totalWater += leftMax - heights[left]
            left += 1
        else:
            if heights[right] >= rightMax:
                rightMax = heights[right]
            else:
                totalWater += rightMax - heights[right]
            right -= 1
    return totalWater