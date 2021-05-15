# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    if not tree:
        return 0
    if tree.left is None and tree.right is None:
        return 0
    leftHeight = getTreeHeight(tree.left)
    rightHeight = getTreeHeight(tree.right)
    withRoot = leftHeight + rightHeight
    withoutRoot = max(binaryTreeDiameter(tree.left), binaryTreeDiameter(tree.right))
    return max(withRoot, withoutRoot)

def getTreeHeight(tree):
    if not tree:
        return 0
    return 1 + max(getTreeHeight(tree.left), getTreeHeight(tree.right))
