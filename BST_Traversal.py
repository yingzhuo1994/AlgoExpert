# O(n) time | O(n) space
def inOrderTraverse(tree, array):
    if not tree:
        return
    inOrderTraverse(tree.left, array)
    array.append(tree.value)
    inOrderTraverse(tree.right, array)
    return array

# O(n) time | O(n) space
def preOrderTraverse(tree, array):
    if not tree:
        return
    array.append(tree.value)
    preOrderTraverse(tree.left, array)
    preOrderTraverse(tree.right, array)
    return array

# O(n) time | O(n) space
def postOrderTraverse(tree, array):
    if not tree:
        return
    postOrderTraverse(tree.left, array)
    postOrderTraverse(tree.right, array)
    array.append(tree.value)
    return array
