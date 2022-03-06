def largestBstSize(tree):
    ans = [0]
    countBST(tree, ans)
    return ans[0]
        
def countBST(node, ans):
    if not node:
        return (0, float("inf"), float("-inf"))
    leftCount, leftLower, leftHigher = countBST(node.left, ans)
    rightCount, rightLower, rightHiger = countBST(node.right, ans)
    ans[0] = max(ans[0], leftCount, rightCount)
    if leftHigher < node.value and node.value <= rightLower:
        count = leftCount + 1 + rightCount
        ans[0] = max(ans[0], count)
        return (count, min(leftLower, node.value), max(rightHiger, node.value))
    else:
        return (0, float("-inf"), float("inf"))

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
