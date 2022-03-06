# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 1st solution
# Average case: when the tree is balanced
# O(n) time | O(h) space
# where n is the number of nodes in the Binary Tree
# and h is the height of the Binary Tree
def largestBstSize(tree):
    ans = [0]
    countBST(tree, ans)
    return ans[0]
        
def countBST(node, ans):
    if not node:
        return (0, float("inf"), float("-inf"))
    leftCount, leftLower, leftHigher = countBST(node.left, ans)
    rightCount, rightLower, rightHiger = countBST(node.right, ans)
    ans[0] = max(ans[0], leftCount, rightCount)
    if leftHigher < node.value and node.value <= rightLower:
        count = leftCount + 1 + rightCount
        ans[0] = max(ans[0], count)
        return (count, min(leftLower, node.value), max(rightHiger, node.value))
    else:
        return (0, float("-inf"), float("inf"))

# 2nd solution, official
# Average case: when the tree is balanced
# O(n) time | O(h) space
# where n is the number of nodes in the Binary Tree
# and h is the height of the Binary Tree
def largestBstSize(tree):
    return getTreeInfo(tree).runningLargestBstSize

def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(
            True,
            float("-inf"),
            float("inf"),
            0,
            0,
        )
    
    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    treeSize = 1 + leftTreeInfo.treeSize + rightTreeInfo.treeSize

    satisfiesBstProp = tree.value > leftTreeInfo.maxValue and tree.value <= rightTreeInfo.minValue
    isBst = satisfiesBstProp and leftTreeInfo.isBst and rightTreeInfo.isBst

    maxValue = max(tree.value, max(leftTreeInfo.maxValue, rightTreeInfo.maxValue))
    minValue = min(tree.value, min(leftTreeInfo.minValue, rightTreeInfo.minValue))

    runningLargestBstSize = 0
    if isBst:
        runningLargestBstSize = treeSize
    else:
        runningLargestBstSize = max(leftTreeInfo.runningLargestBstSize, rightTreeInfo.runningLargestBstSize)
    
    return TreeInfo(
        isBst,
        maxValue,
        minValue,
        runningLargestBstSize,
        treeSize,
    )

class TreeInfo:
    def __init__(self, isBst, maxValue, minValue, runningLargestBstSize, treeSize):
        self.isBst = isBst
        self.maxValue = maxValue
        self.minValue = minValue
        self.runningLargestBstSize = runningLargestBstSize
        self.treeSize = treeSize