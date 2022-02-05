# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# 1st solution
# O(n^2) time | O(n) space - where n is the length of the input array
def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    n = len(preOrderTraversalValues)
    if n == 0:
        return None
    
    currentValue = preOrderTraversalValues[0]
    rightSubtreeRootIdx = n

    for idx in range(1, n):
        value = preOrderTraversalValues[idx]
        if value >= currentValue:
            rightSubtreeRootIdx = idx
            break
    
    leftSubtree = reconstructBst(preOrderTraversalValues[1:rightSubtreeRootIdx])
    rightSubtree = reconstructBst(preOrderTraversalValues[rightSubtreeRootIdx:])
    return BST(currentValue, leftSubtree, rightSubtree)

# 2nd solution
# O(n) time | O(n) space
# where n is the length of the input array
def reconstructBst(preOrderTraversalValues):
    treeInfo = TreeInfo(0)
    return reconstructBstFromRange(float('-inf'), float('inf'), preOrderTraversalValues, treeInfo)

def reconstructBstFromRange(lowerBound, upperBound, preOrderTraversalValues, curSubtreeInfo):
    if curSubtreeInfo.rootIdx == len(preOrderTraversalValues):
        return None

    rootValue = preOrderTraversalValues[curSubtreeInfo.rootIdx]
    if rootValue < lowerBound or rootValue >= upperBound:
        return None

    curSubtreeInfo.rootIdx += 1
    leftSubtree = reconstructBstFromRange(lowerBound, rootValue, preOrderTraversalValues, curSubtreeInfo)
    rightSubtree = reconstructBstFromRange(rootValue, upperBound, preOrderTraversalValues, curSubtreeInfo)
    return BST(rootValue, leftSubtree, rightSubtree)

class TreeInfo:
    def __init__(self, rootIdx):
        self.rootIdx = rootIdx