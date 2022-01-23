# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def allKindsOfNodeDepths(root):
    ans = 0
    stack = [(root, 0)]
    while stack:
        node, depth = stack.pop()
        if node is not None:
            ans += (1 + depth) * depth // 2
            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))
    return ans
