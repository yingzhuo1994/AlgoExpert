def invertBinaryTree(tree):
    # Write your code here.
    # O(n)
    if not tree:
        return None
    tree.left, tree.right = tree.right, tree.left
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)



# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
