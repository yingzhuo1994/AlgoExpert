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
    lst = preOrderTraversalValues
    n = len(lst)
    if n == 0:
        return None
    tree = BST(lst[0])
    k = 1
    while k < n:
        if lst[k] >= lst[0]:
            break
        k += 1
    tree.left = reconstructBst(lst[1:k])
    tree.right = reconstructBst(lst[k:])
    return tree

# 2nd solution
class TreeInfo:
    def __init__(self, rootIdx):
        self.rootIdx = rootIdx

def reconstructBst(preOrderTraversalValues):
    treeInfo = TreeInfo(0)
    return reconstructBstFromRange(float('-inf'), float('inf'), preOrderTraversalValues, treeInfo)

def reconstructBstFromRange(lowerBound, upperBound, lst, curSubtreeInfo):
    if curSubtreeInfo.rootIdx == len(lst):
        return None

    rootValue = lst[curSubtreeInfo.rootIdx]
    if rootValue < lowerBound or rootValue >= upperBound:
        return None

    curSubtreeInfo.rootIdx += 1
    leftSubtree = reconstructBstFromRange(lowerBound, rootValue, lst, curSubtreeInfo)
    rightSubtree = reconstructBstFromRange(rootValue, upperBound, lst, curSubtreeInfo)
    return BST(rootValue, leftSubtree, rightSubtree)
