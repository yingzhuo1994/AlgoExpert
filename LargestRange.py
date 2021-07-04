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




