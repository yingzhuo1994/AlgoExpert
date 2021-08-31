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

# 2nd solution
# O(n) time | O(n) space
def waterArea(heights):
    maxes = [0 for x in heights]
    leftMax = 0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = leftMax
        leftMax = max(leftMax, height)
    rightMax = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        minHeight = min(rightMax, maxes[i])
        if height < minHeight:
            maxes[i] = minHeight - height
        else:
            maxes[i] = 0
        rightMax = max(rightMax, height)
    return sum(maxes)