# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(n) time | O(d) space
def validateBst(tree):
    # Write your code here.
    return validateBstHelper(tree, float('-inf'), float('inf'))

def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    leftIsValid = validateBstHelper(tree.left, minValue, tree.value)
    if not leftIsValid:
        return False
    rightIsValid = validateBstHelper(tree.right, tree.value, maxValue)
    return rightIsValid
