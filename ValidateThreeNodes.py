# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 1st solution
# O(h) time | O(h) space - where h is the height of the tree
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.
    if isDescendant(nodeOne, nodeTwo):
		return isDescendant(nodeTwo, nodeThree)
    elif isDescendant(nodeThree, nodeTwo):
		return isDescendant(nodeTwo, nodeOne)
    else:
        return False

def isDescendant(ancestor, descendant):
    if not ancestor:
        return False
    if ancestor == descendant:
        return True
    if descendant.value < ancestor.value:
        return isDescendant(ancestor.left, descendant)
    else:
        return isDescendant(ancestor.right, descendant)