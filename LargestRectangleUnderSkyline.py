# 1st solution
# O(n) time | O(n) space
def largestRectangleUnderSkyline(buildings):
    buildings.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(buildings)):
        while stack and buildings[stack[-1]] > buildings[i]:
            h = buildings[stack.pop()]
            w = i - stack[-1] - 1
            area = h * w
            ans = max(area, ans)
        stack.append(i)
    buildings.pop()
    return ans