# 1st solution
def largestRange(array):
    arraySet = set(array)
    largestPair = [0, -1]
    for num in arraySet:
        if num - 1 not in arraySet:
            start = num
            end = num
            curNum = num
            while curNum + 1 in arraySet:
                curNum += 1
                end = curNum
            if end - start > largestPair[1] - largestPair[0]:
                largestPair = [start, end]
    return largestPair

# 2nd solution
# O(n) time | O(n) space
def largestRange(array):
    bestRange = []
    longestLength = 0
    nums = {}
    for num in array:
        nums[num] = True
    for num in array:
        if not nums[num]:
            continue
        nums[num] = False
        currentLength = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False
            currentLength += 1
            left -= 1
        while right in nums:
            nums[right] = False
            currentLength += 1
            right += 1
        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left + 1, right - 1]
    return bestRange
            
