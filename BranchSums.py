class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    if not root:
        return []
    if root.left is None and root.right is None:
        return [root.value]
    a = [root.value + v for v in branchSums(root.left)]
    b = [root.value + v for v in branchSums(root.right)]
    return a + b

tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.right = BinaryTree(3)

print(branchSums(tree))
