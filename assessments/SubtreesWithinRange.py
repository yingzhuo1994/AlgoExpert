# 1st solution, TLE
def subtreesWithinRange(tree, targetRange):
    treeInfo = getSubTreeInfo(tree, targetRange)
    return treeInfo.count

def getSubTreeInfo(tree, targetRange):
    if not tree:
        return TreeInfo(0, [targetRange[1], targetRange[0]])
    
    value = tree.value
    finalRange = [float("-inf"), float("inf")]
    leftSubtreeInfo = getSubTreeInfo(tree.left, targetRange) if value >= targetRange[0] else TreeInfo(0, finalRange)
    rightSubtreeInfo = getSubTreeInfo(tree.right, targetRange) if value <= targetRange[1] else TreeInfo(0, finalRange)
    count = leftSubtreeInfo.count + rightSubtreeInfo.count
    isLeftSubtreeValid = leftSubtreeInfo.range[0] >= targetRange[0]
    isRightSubtreeValid = rightSubtreeInfo.range[1] <= targetRange[1]

    if isLeftSubtreeValid and isRightSubtreeValid:
        largest = max(rightSubtreeInfo.range[1], value)
        smallest = min(leftSubtreeInfo.range[0], value)
        finalRange = [smallest, largest]
        count += 1
    return TreeInfo(count, finalRange)
    
class TreeInfo:
    def __init__(self, count, range):
        self.count = count
        self.range = range

# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 2nd solution
# Average case: when the tree is balanced
# O(n) time | O(h) space
# where n is the number of nodes in the BST and h is the height of the BST
def subtreesWithinRange(tree, targetRange):
    return getTreeInfo(tree, targetRange).numSubtreesWithinRange

def getTreeInfo(tree, targetRange):
    numSubtreesWithinRange = 0
    maxValue = tree.value
    minValue = tree.value

    if tree.left is not None:
        leftSubtreeInfo = getTreeInfo(tree.left, targetRange)
        minValue = leftSubtreeInfo.minValue
        numSubtreesWithinRange += leftSubtreeInfo.numSubtreesWithinRange
    
    if tree.right is not None:
        rightSubtreeInfo = getTreeInfo(tree.right, targetRange)
        maxValue = rightSubtreeInfo.maxValue
        numSubtreesWithinRange += rightSubtreeInfo.numSubtreesWithinRange
    
    if minValue >= targetRange[0] and maxValue <= targetRange[1]:
        numSubtreesWithinRange += 1
    
    return TreeInfo(
        maxValue,
        minValue,
        numSubtreesWithinRange,
    )

class TreeInfo:
    def __init__(self, maxValue, minValue, numSubtreesWithinRange):
        self.maxValue = maxValue
        self.minValue = minValue
        self.numSubtreesWithinRange = numSubtreesWithinRange   

# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 3rd solution
# Average case: when the tree is balanced
# O(n) time | O(h) space
# where n is the number of nodes in the BST and h is the height of the BST
def subtreesWithinRange(tree, targetRange):
    answer = {"result": 0}
    isTreeWithinRange(tree, targetRange, answer)
    return answer["result"]

def isTreeWithinRange(tree, targetRange, answer):
    if tree is None:
        return True
    
    leftTreeWithinRange = isTreeWithinRange(tree.left, targetRange, answer)
    rightTreeWithinRnage = isTreeWithinRange(tree.right, targetRange, answer)
    nodeInRange = tree.value >= targetRange[0] and tree.value <= targetRange[1]
    treeWithinRange = leftTreeWithinRange and rightTreeWithinRnage and nodeInRange

    if treeWithinRange:
        answer["result"] += 1
    
    return treeWithinRange

# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None