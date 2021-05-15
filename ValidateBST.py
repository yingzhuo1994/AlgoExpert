# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    return helper(tree, float('-inf'), float('inf'))

def helper(tree, minValue, maxValue):
    if not tree:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = helper(tree.left, minValue, tree.value)
    rightIsValid = helper(tree.right, tree.value, maxValue)
    return leftIsValid and rightIsValid
