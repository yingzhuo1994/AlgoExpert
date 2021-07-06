# 1st solution
def taskAssignment(k, tasks):
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

# 2nd solution
# O(nlogn) time | O(n) space - where n is the number of tasks
def taskAssignment(k, tasks):
    pairedTasks = []
    taskDurationsToIndices = getTaskDurationsToIndices(tasks)

    sortedTasks = sorted(tasks)
    for idx in range(k):
        taskOneDuration = sortedTasks[idx]
        indicesWithTaskOneDuration = taskDurationsToIndices[taskOneDuration]
        taskOneIndex = indicesWithTaskOneDuration.pop()

        taskTwoSortedIndex = len(tasks) - 1 - idx
        taskTwoDuration = sortedTasks[taskTwoSortedIndex]
        indicesWithTaskTwoDuration = taskDurationsToIndices[taskTwoDuration]
        taskTwoIndex = indicesWithTaskTwoDuration.pop()

        pairedTasks.append([taskOneIndex, taskTwoIndex])
    
    return pairedTasks

def getTaskDurationsToIndices(tasks):
    taskDurationsToIndices = {}

    for idx, taskDuration in enumerate(tasks):
        if taskDuration in taskDurationsToIndices:
            taskDurationsToIndices[taskDuration].append(idx)
        else:
            taskDurationsToIndices[taskDuration] = [idx]
    
    return taskDurationsToIndices

# 3rd solution
# O(nlogn) time | O(n) space - where n is the number of tasks
def taskAssignment(k, tasks):
    dic = {}
	for i, num in enumerate(tasks):
		dic[num] = dic.get(num, []) + [i]
	lst  = sorted(tasks)
	result = []
	for i in range(len(lst) // 2):
		first = dic[lst[i]].pop()
		second = dic[lst[len(lst) - 1 - i]].pop()
		result.append([first, second])
	return result