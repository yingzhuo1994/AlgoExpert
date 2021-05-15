def threeNumberSum(array, targetSum):
    # Write your code here.
    # brute-force search
    n = len(array)
    if n < 3:
        return None
    array.sort()
    lst = []
    # for p1 in range(n - 2):
    #     for p2 in range(p1 + 1, n - 1):
    #         for p3 in range(p2 + 1, n):
    #             temp = [array[p1], array[p2], array[p3]]
    #             if sum(temp) == targetSum:
    #                 lst.append(temp)
    # return lst

    # 2nd Solution
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            temp = [array[i], array[left], array[right]]
            curSum = sum(temp)
            if curSum == targetSum:
                lst.append(temp)
                left += 1
                right -= 1
            elif curSum > targetSum:
                right -= 1
            else:
                left += 1
    return lst
