# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# 1st solution
# O(m + n) time | O(h1 + h2) space
def compareLeafTraversal(tree1, tree2):
    one = getLeaves(tree1)
    two = getLeaves(tree2)
    if len(one) != len(two):
        return False
    for i in range(len(one)):
        if one[i] != two[i]:
            return False
    return True

def getLeaves(tree):
    leaves = []
    stack = []
    node = tree
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        if node is None:
            continue
        if not node.left and not node.right:
            leaves.append(node.value)
        node = node.right
    return leaves

# 2nd solution
# O(m + n) time | O(h1 + h2) space
# where n is the number of nodes in the first Binary Tree, m is the number in the second,
# h1 is the height of the first Binary Tree, and h2 is the height of the second
def compareLeafTraversal(tree1, tree2):
    tree1TraversalStack = [tree1]
    tree2TraversalStack = [tree2]

    while len(tree1TraversalStack) > 0 and len(tree2TraversalStack) > 0:
        tree1Leaf = getNextLeafNode(tree1TraversalStack)
        tree2Leaf = getNextLeafNode(tree2TraversalStack)

        if tree1Leaf.value != tree2Leaf.value:
            return False
        
    return len(tree1TraversalStack) == 0 and len(tree2TraversalStack) == 0

def getNextLeafNode(traversalStack):
    currentNode = traversalStack.pop()

    while not isLeafNode(currentNode):
        if currentNode.right is not None:
            traversalStack.append(currentNode.right)
        
        if currentNode.left is not None:
            traversalStack.append(currentNode.left)
        
        currentNode = traversalStack.pop()
    
    return currentNode

def isLeafNode(node):
    return node.left is None and node.right is None

# 3rd solution
# O(m + n) time | O(max(h1 + h2)) space
# where n is the number of nodes in the first Binary Tree, m is the number in the second,
# h1 is the height of the first Binary Tree, and h2 is the height of the second
def compareLeafTraversal(tree1, tree2):
    tree1LeafNodesLinkedList, _ = connectLeafNodes(tree1)
    tree2LeafNodesLinkedList, _ = connectLeafNodes(tree2)

    list1CurrentNode = tree1LeafNodesLinkedList
    list2CurrentNode = tree2LeafNodesLinkedList
    while list1CurrentNode is not None and list2CurrentNode is not None:
        if list1CurrentNode.value != list2CurrentNode.value:
            return False
        
        list1CurrentNode = list1CurrentNode.right
        list2CurrentNode = list2CurrentNode.right

    return list1CurrentNode is None and list2CurrentNode is None

def connectLeafNodes(currentNode, head=None, previousNode=None):
    if currentNode is None:
        return head, previousNode
    
    if isLeafNode(currentNode):
        if previousNode is None:
            head = currentNode
        else:
            previousNode.right = currentNode
        
        previousNode = currentNode
    
    leftHead, leftPreviousNode = connectLeafNodes(currentNode.left, head, previousNode)
    return connectLeafNodes(currentNode.right, leftHead, leftPreviousNode)

def isLeafNode(node):
    return node.left is None and node.right is None