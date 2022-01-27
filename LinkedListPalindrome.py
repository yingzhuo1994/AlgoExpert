# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# 1st solution
# O(n) time | O(n) space
def linkedListPalindrome(head):
    stack = []
    while head:
        stack.append(head.value)
        head = head.next
    left, right = 0, len(stack) - 1
    while left < right:
        if stack[left] != stack[right]:
            return False
        left += 1
        right -= 1
    return True

# 2nd solution
# O(n) time | O(n) space
# where n is the number of nodes in the Linked List
def linkedListPalindrome(head):
    isPalindromeResults = isPalindrome(head, head)
    return isPalindromeResults.outerNodesAreEqual

def isPalindrome(leftNode, rightNode):
    if rightNode is None:
        return LinkedListInfo(True, leftNode)
    
    recursiveCallResults = isPalindrome(leftNode, rightNode.next)
    leftNodeToCompare = recursiveCallResults.leftNodeToCompare
    outerNodesAreEqual = recursiveCallResults.outerNodesAreEqual

    recursiveIsEqual = outerNodesAreEqual and leftNodeToCompare.value == rightNode.value
    nextLeftNodeToCompare = leftNodeToCompare.next

    return LinkedListInfo(recursiveIsEqual, nextLeftNodeToCompare)

class LinkedListInfo:
    def __init__(self, outerNodesAreEqual, leftNodeToCompare):
        self.outerNodesAreEqual = outerNodesAreEqual
        self.leftNodeToCompare = leftNodeToCompare

# 3rd solution
# O(n) time | O(n) space
# where n is the number of nodes in the Linked List
def linkedListPalindrome(head):
    slowNode = head
    fastNode = head
    while fastNode is not None and fastNode.next is not None:
        slowNode = slowNode.next
        fastNode = fastNode.next.next
    
    reversedSecondHalfNode = reverseLinkedList(slowNode)
    firstHalfNode = head
    
    while reversedSecondHalfNode is not None:
        if reversedSecondHalfNode.value != firstHalfNode.value:
            return False
        reversedSecondHalfNode = reversedSecondHalfNode.next
        firstHalfNode = firstHalfNode.next
    
    return True

def reverseLinkedList(head):
    previousNode, currentNode = None, head
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next=  previousNode
        previousNode = currentNode
        currentNode =nextNode
    return previousNode