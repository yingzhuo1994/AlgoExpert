# 1st brute-force solution
# O(n^2) time | O(n) space
def nextGreaterElement(array):
    # Write your code here.
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
