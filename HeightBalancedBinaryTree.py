# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# 1st solution
def heightBalancedBinaryTree(tree):
    # Write your code here.
    if not tree:
        return True
    if tree.left is None and tree.right is None:
        return True
    leftHeight = getHeight(tree.left)
    rightHeight = getHeight(tree.right)
    if abs(leftHeight - rightHeight) > 1:
        return False
    return heightBalancedBinaryTree(tree.left) and heightBalancedBinaryTree(tree.right)

def getHeight(tree):
    if not tree:
        return 0
    return 1 + max(getHeight(tree.left), getHeight(tree.right))

# 2nd solution
class treeInfo:
    def __init__(self, isBalanced, height):
        self.isBalanced = isBalanced
        self.height = height

def heightBalancedBinaryTree(tree):
    # Write your code here.
    return getTreeInfo(tree).isBalanced

def getTreeInfo(node):
    if not node:
        return treeInfo(True, -1)

    leftSubTreeInfo = getTreeInfo(node.left)
    rightSubTreeInfo = getTreeInfo(node.right)
    isBalanced = leftSubTreeInfo.isBalanced and rightSubTreeInfo.isBalanced and (
                    abs(leftSubTreeInfo.height - rightSubTreeInfo.height) <= 1)
    height = 1 + max(leftSubTreeInfo.height, rightSubTreeInfo.height)
    return treeInfo(isBalanced, height)
