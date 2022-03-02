# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# 1st solution
# O(n) time | o(1) space
def invertedBisection(head):
    slow = fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    if prev is not None:
        prev.next = None
    if fast is None:
        # even number
        middle = None
    else:
        # odd number
        middle = slow 
        slow = slow.next
        middle.next = None
    firstHead = reverseLinkedList(head)
    secondHead = reverseLinkedList(slow)
    if middle is None:
        head.next = secondHead
    else:
        head.next = middle
        middle.next = secondHead
    return firstHead
    

def reverseLinkedList(head):
    prev = None
    node = head
    while node:
        nextNode = node.next
        node.next = prev
        prev = node
        node = nextNode
    return prev

# 2nd solution
# O(n) time | o(1) space
def invertedBisection(head):
    length = getLinkedListLength(head)
    if length <= 3:
        return head
    
    firstHalfTail = getMiddleNode(head, length)
    middleNode = None
    secondHalfHead = None
    if length % 2 == 0:
        secondHalfHead = firstHalfTail.next
    else:
        middleNode = firstHalfTail.next
        secondHalfHead = firstHalfTail.next.next
    
    firstHalfTail.next = None
    reverseLinkedList(head)
    reversedSecondHalfHead = reverseLinkedList(secondHalfHead)

    if middleNode is None:
        head.next = reversedSecondHalfHead
    else:
        head.next = middleNode
        middleNode.next = reversedSecondHalfHead
    
    return firstHalfTail

def getLinkedListLength(head):
    length = 0
    currentNode = head
    while currentNode is not None:
        currentNode = currentNode.next
        length += 1
    return length

def getMiddleNode(head, length):
    halfLength = length // 2
    currentPosition = 1
    currentNode = head
    while currentPosition != halfLength:
        currentNode = currentNode.next
        currentPosition += 1
    return currentNode

def reverseLinkedList(head):
    previousNode, currentNode = None, head
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    return previousNode