# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# 1st solution
# O(n) time | O(n) space
def compareLeafTraversal(tree1, tree2):
    one = getLeaves(tree1)
    two = getLeaves(tree2)
    if len(one) != len(two):
        return False
    for i in range(len(one)):
        if one[i] != two[i]:
            return False
    return True

def getLeaves(tree):
    leaves = []
    stack = []
    node = tree
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        if node is None:
            continue
        if not node.left and not node.right:
            leaves.append(node.value)
        node = node.right
    return leaves
