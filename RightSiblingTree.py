# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# 1st solution
# O(n) time | O(n) space
def rightSiblingTree(root):
    level = [root]
    while level:
        newLevel = []
        for i, node in enumerate(level):
            if node is None:
                continue
            newLevel.append(node.left)
            newLevel.append(node.right)
            if i + 1 >= len(level) or level[i + 1] is None:
                level[i].right = None
            else:
                level[i].right = level[i + 1]
        level = newLevel
    return root

# 2nd solution
# O(n) time | O(d) space - where n is the number of nodes in the Binary Tree and d is the depth (height) of the Binary Tree
def rightSiblingTree(root):
    mutate(root, None, None)
    return root

def mutate(node, parent, isLeftChild):
    if node is None:
        return
    left, right = node.left, node.right
    mutate(left, node, True)
    if parent is None:
        node.right = None
    elif isLeftChild:
        node.right = parent.right
    else:
        if parent.right is None:
            node.right = None
        else:
            node.right = parent.right.left
    mutate(right, node, False)
