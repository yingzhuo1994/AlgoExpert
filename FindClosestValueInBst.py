# def findClosestValueInBst(tree, target):
#     # Write your code here.
#     dic = {}
#     def helper(tree, target):
#         nonlocal dic
#         if not tree:
#             return
#         dic[tree.value] = abs(target - tree.value)
#         if target == tree.value:
#             return
#         elif target < tree.value:
#             helper(tree.left, target)
#         else:
#             helper(tree.right, target)
#     helper(tree, target)
#     return min(dic, key = lambda k: dic[k])

def findClosestValueInBst(tree, target):
    # Write your code here.
    currentNode = tree
    closest = currentNode.value

    while currentNode is not None:
        if abs(closest - target) > abs(currentNode.value - target):
            closest = currentNode.value
        if target == currentNode.value:
            break
        elif target < currentNode.value:
            currentNode = currentNode.left
        else:
            currentNode = currentNode.right
    return closest


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
