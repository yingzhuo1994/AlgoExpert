# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# 1st solution
def findSuccessor(tree, node):
    # Write your code here.
    array = inOrderTraversal(tree)
    for i in range(len(array) - 1):
        if array[i] == node:
            return array[i + 1]
    return None

def inOrderTraversal(tree, array = []):
    if not tree:
        return []
    inOrderTraversal(tree.left)
    array.append(tree)
    inOrderTraversal(tree.right)
    return array

# 2nd solution
def findSuccessor(tree, node):
    # Write your code here.
    if node.right:
        p = node.right
        while p.left:
            p = p.left
        return p
    else:
        p = node
        while p.parent and p.parent.right == p:
            p = p.parent
        return p.parent
