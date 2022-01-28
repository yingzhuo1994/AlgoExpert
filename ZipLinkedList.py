# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def zipLinkedList(linkedList):
    slowNode = linkedList
    fastNode = linkedList
    prev = LinkedList
    while fastNode and fastNode.next:
        prev = slowNode
        slowNode = slowNode.next
        fastNode = fastNode.next.next
    
    firstHalf = linkedList
    secondHalf = reverseLinkedList(slowNode)
    prev.next = None
    
    while firstHalf:
        nextFirstHalf = firstHalf.next
        nextSecondHalf = secondHalf.next
        firstHalf.next = secondHalf
        secondHalf.next = nextFirstHalf or nextSecondHalf
        firstHalf = nextFirstHalf
        secondHalf = nextSecondHalf
    return linkedList
    
def reverseLinkedList(head):
    previousNode, currentNode = None, head
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next=  previousNode
        previousNode = currentNode
        currentNode = nextNode
    return previousNode

def printLinkedList(head):
    stack = []
    while head:
        stack.append(head.value)
        head = head.next
    print(stack)