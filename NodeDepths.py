# 1st solution, Recursion
# O(n) time | O(h) space 
def nodeDepths(root):
    # Write your code here.
    return singleNodeDepth(root, 0)

def singleNodeDepth(tree, depth):
	if not tree:
		return 0
	else:
		return depth + singleNodeDepth(tree.left, depth + 1) + singleNodeDepth(tree.right, depth + 1)

# 2nd solution, Iteration
# O(n) time | O(h) space 
def nodeDepths(root):
	stack = [(root, 0)]
	ans = 0
	while stack:
		node, depth = stack.pop()
		ans += depth
		if node.right:
			stack.append((node.right, depth + 1))
		if node.left:
			stack.append((node.left, depth + 1))
	return ans

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
