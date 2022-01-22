# 1st solution
def rightSmallerThan(array):
    ans = [0 for _ in array]
    arr = [[array[i], i] for i in range(len(array))]
    mergeSort(arr, ans)
    return ans

def mergeSort(array, ans):
    if len(array) <= 1:
        return array
    half = len(array) // 2
    left = mergeSort(array[:half], ans)
    right = mergeSort(array[half:], ans)
    newArray = []
    for i in range(len(left)):
        for j in range(len(right)):
            if left[i][0] > right[j][0]:
                ans[left[i][1]] += 1

    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            newArray.append(left[i])
            i += 1
        else:
            newArray.append(right[j])
            j += 1
    newArray.extend(left[i:] or right[j:])
    return newArray    
    
# 2nd solution
# Average case: when the created BST is balanced
# O(nlog(n)) time | O(n) space - where n is the length of the array
# ---
# Worst case: when the created BST is like a linked list
# O(n^2) time | O(n) space
def rightSmallerThan(array):
    if len(array) == 0:
        return []
    
    lastIdx = len(array) - 1
    bst = SpecialBST(array[lastIdx], lastIdx, 0)
    for i in reversed(range(len(array) - 1)):
        bst.insert(array[i], i)
    
    rightSmallerCounts = array[:]
    getRightSmallerCounts(bst, rightSmallerCounts)
    return rightSmallerCounts

def getRightSmallerCounts(bst, rightSmallerCounts):
    if bst is None:
        return
    rightSmallerCounts[bst.idx] = bst.numSmallerAtInsertTime
    getRightSmallerCounts(bst.left, rightSmallerCounts)
    getRightSmallerCounts(bst.right, rightSmallerCounts)

class SpecialBST:
    def __init__(self, value, idx, numSmallerAtInsertTime):
        self.value = value
        self.idx = idx
        self.numSmallerAtInsertTime = numSmallerAtInsertTime
        self.leftSubtreeSize = 0
        self.left = None
        self.right = None
    
    def insert(self, value, idx, numSmallerAtInsertTime = 0):
        if value < self.value:
            self.leftSubtreeSize += 1
            if self.left is None:
                self.left = SpecialBST(value, idx, numSmallerAtInsertTime)
            else:
                self.left.insert(value, idx, numSmallerAtInsertTime)
        else:
            numSmallerAtInsertTime += self.leftSubtreeSize
            if value > self.value:
                numSmallerAtInsertTime += 1
            if self.right is None:
                self.right = SpecialBST(value, idx, numSmallerAtInsertTime)
            else:
                self.right.insert(value, idx, numSmallerAtInsertTime)

# 3rd solution
# Average case: when the created BST is balanced
# O(nlog(n)) time | O(n) space - where n is the length of the array
# ---
# Worst case: when the created BST is like a linked list
# O(n^2) time | O(n) space
def rightSmallerThan(array):
    if len(array) == 0:
        return []
    
    rightSmallerCounts = array[:]
    lastIdx = len(array) - 1
    bst = SpecialBST(array[lastIdx])
    rightSmallerCounts[lastIdx] = 0
    for i in reversed(range(len(array) - 1)):
        bst.insert(array[i], i, rightSmallerCounts)
    
    return rightSmallerCounts

class SpecialBST:
    def __init__(self, value):
        self.value = value
        self.leftSubtreeSize = 0
        self.left = None
        self.right = None
    
    def insert(self, value, idx, rightSmallerCounts, numSmallerAtInsertTime = 0):
        if value < self.value:
            self.leftSubtreeSize += 1
            if self.left is None:
                self.left = SpecialBST(value)
                rightSmallerCounts[idx] = numSmallerAtInsertTime
            else:
                self.left.insert(value, idx, rightSmallerCounts, numSmallerAtInsertTime)
        else:
            numSmallerAtInsertTime += self.leftSubtreeSize
            if value > self.value:
                numSmallerAtInsertTime += 1
            if self.right is None:
                self.right = SpecialBST(value)
                rightSmallerCounts[idx] = numSmallerAtInsertTime
            else:
                self.right.insert(value, idx, rightSmallerCounts, numSmallerAtInsertTime)