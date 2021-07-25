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
    if ancestor is descendant:
        return True
    if descendant.value < ancestor.value:
        return isDescendant(ancestor.left, descendant)
    else:
        return isDescendant(ancestor.right, descendant)

# 2nd solution
# O(h) time | O(1) space - where h is the height of the tree
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.
    if isDescendant(nodeOne, nodeTwo):
        return isDescendant(nodeTwo, nodeThree)
    elif isDescendant(nodeThree, nodeTwo):
        return isDescendant(nodeTwo, nodeOne)
    else:
        return False

def isDescendant(ancestor, descendant):
    while ancestor and ancestor is not descendant:
        if descendant.value < ancestor.value:
            ancestor = ancestor.left
        else:
            ancestor = ancestor.right
    return descendant is ancestor

# 3rd solution
# O(d) time | O(1) space - where d is the distance between nodeOne and nodeThree
def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    searchOne = nodeOne
    searchTwo = nodeThree

    while True:
        foundThreeFromOne = searchOne is nodeThree
        foundOneFromThree = searchTwo is nodeOne
        foundNodeTwo = searchOne is nodeTwo or searchTwo is nodeTwo
        finishedSearching = searchOne is None and searchTwo is None
        if foundThreeFromOne or foundOneFromThree or foundNodeTwo or finishedSearching:
            break

        if searchOne:
            if searchOne.value > nodeTwo.value :
                searchOne = searchOne.left
            else:
                searchOne = searchOne.right
        
        if searchTwo:
            if searchTwo.value > nodeTwo.value:
                searchTwo = searchTwo.left
            else:
                searchTwo = searchTwo.right
        
    foundNodeFromOther = searchOne is nodeThree or searchTwo is nodeOne
    # foundNodeTwo = searchOne is nodeTwo or searchTwo is nodeTwo
    if not foundNodeTwo or foundNodeFromOther:
        return False
    
    return searchForTarget(nodeTwo, nodeThree if searchOne is nodeTwo else nodeOne)

def searchForTarget(node, target):
    while node is not None and node is not target:
        if target.value < node.value:
            node = node.left
        else:
            node = node.right
    return node is target