def nSum(array, n, target):
    if len(array) < n:
        return None
    lst = []
    if n == 1:
        lst = [[num] for num in array if num == target]
    elif n == 2:
        dic = {}
        for i, num in enumerate(array):
            curGoal = target - num
            if curGoal in dic:
                temp = [curGoal, num]
                lst.append(temp)
            else:
                dic[num] = i
    else:
        for i, num in enumerate(array):
            curGoal = target - num
            lastSumLst = nSum(array[i+1:], n-1, curGoal)
            if lastSumLst is not None:
                temp = [[num] + t for t in lastSumLst]
                lst.extend(temp)
    return lst

array = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0
n = 4
result = nSum(array, n, target)
print(result)
