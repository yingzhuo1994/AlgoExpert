# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# 1st solution
# O(n) time | O(n) space
def flattenBinaryTree(root):
    stack = []
    cur = root
    ans = []
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        node = stack.pop()
        ans.append(node)
        cur = node.right
        
    for i in range(len(ans) - 1):
        ans[i].right = ans[i + 1]
        ans[i + 1].left = ans[i]
    return ans[0]