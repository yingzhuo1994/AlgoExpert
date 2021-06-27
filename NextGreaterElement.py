<<<<<<< HEAD
# 1st brute-force solution
# O(n^2) time | O(n) space
=======
>>>>>>> 48abe7919a41defbc64e6b1ddce011f9a3e1d636
def nextGreaterElement(array):
    # Write your code here.
    newArray = []
    for i in range(len(array)):
        newArray.append(getNextGreaterElement(array, i))
<<<<<<< HEAD
	return newArray
=======
    return newArray
>>>>>>> 48abe7919a41defbc64e6b1ddce011f9a3e1d636

def getNextGreaterElement(array, idx):
    for i in range(idx + 1, len(array)):
        if array[i] > array[idx]:
            return array[i]
    for i in range(idx):
        if array[i] > array[idx]:
            return array[i]
<<<<<<< HEAD
    return -1
=======
    return -1
>>>>>>> 48abe7919a41defbc64e6b1ddce011f9a3e1d636
