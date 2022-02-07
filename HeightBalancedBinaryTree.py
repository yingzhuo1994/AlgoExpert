# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# 1st solution
# O(n) time | O(h) space
# where n is the number of nodes in the binary tree
def heightBalancedBinaryTree(tree):
    height, isBalanced = getHeightOfTree(tree)
    return isBalanced

def getHeightOfTree(node):
    if not node:
        return (0, True)
    leftHeight, isLeftBalanced = getHeightOfTree(node.left)
    rightHeight, isRightBalanced = getHeightOfTree(node.right)
    height = 1 + max(leftHeight, rightHeight)
    isBalanced = isLeftBalanced and isRightBalanced and abs(leftHeight - rightHeight) <= 1
    return (height, isBalanced)

# 2nd solution
# O(n) time | O(h) space
# where n is the number of nodes in the binary tree
class TreeInfo:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height

def heightBalancedBinaryTree(tree):
    treeInfo = getTreeInfo(tree)
    return treeInfo.isBalanced

def getTreeInfo(node):
    if node is None:
        return TreeInfo(True, -1)

    leftSubTreeInfo = getTreeInfo(node.left)
    rightSubTreeInfo = getTreeInfo(node.right)

    isBalanced = (
        leftSubTreeInfo.isBalanced 
        and rightSubTreeInfo.isBalanced 
        and abs(leftSubTreeInfo.height - rightSubTreeInfo.height) <= 1
    )
    height = 1 + max(leftSubTreeInfo.height, rightSubTreeInfo.height)
    return TreeInfo(isBalanced, height)