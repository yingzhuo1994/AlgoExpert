def nodeDepths(root):
    # Write your code here.
    return singleNodeDepth(root, 0)

def singleNodeDepth(tree, depth):
	if not tree:
		return 0
	else:
		return depth + singleNodeDepth(tree.left, depth + 1) + singleNodeDepth(tree.right, depth + 1)

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
