def taskAssignment(k, tasks):
    # Write your code here.
    indexInOrder = []
    count = 0
    smallestIndex = 0
    while count < len(tasks):
        for i in range(len(tasks)):
            if i not in indexInOrder and tasks[i] < tasks[smallestIndex]:
                smallestIndex = i
        indexInOrder.append(smallestIndex)
        for k in range(len(tasks)):
            if k not in indexInOrder:
                smallestIndex = k
                break
        count += 1
    result = []
    start, end = 0, len(tasks) - 1
    while start < end:
        result.append([indexInOrder[start], indexInOrder[end]])
        start += 1
        end -= 1
    return result
