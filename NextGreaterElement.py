# 1st brute-force solution
# O(n^2) time | O(n) space
def nextGreaterElement(array):
    newArray = []
    for i in range(len(array)):
        newArray.append(getNextGreaterElement(array, i))
	return newArray

def getNextGreaterElement(array, idx):
    for i in range(idx + 1, len(array)):
        if array[i] > array[idx]:
            return array[i]
    for i in range(idx):
        if array[i] > array[idx]:
            return array[i]
    return -1

# 2nd solution
# O(n) time | O(n) space
def nextGreaterElement(array):
    result = [-1] * len(array)
    stack = []

    for idx in range(2 * len(array)):
        circularIdx = idx % len(array)

        while len(stack) > 0 and array[stack[-1]] < array[circularIdx]:
            top = stack.pop()
            result[top] = array[circularIdx]
        
        stack.append(circularIdx)

    return result

# 3rd solution
# O(n) time | O(n) space
def nextGreaterElement(array):
    result = [-1] * len(array)
    stack = []

    for idx in range(2 * len(array) - 1, -1, -1):
        circularIdx = idx % len(array)

        while len(stack) > 0:
            if stack[len(stack) - 1] <= array[circularIdx]:
                stack.pop()
            else:
                result[circularIdx] = stack[len(stack) - 1]
                break
        
        stack.append(array[circularIdx])

    return result