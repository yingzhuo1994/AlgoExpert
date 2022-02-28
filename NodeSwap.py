# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# 1st solution
# O(n) time | O(1) space
def nodeSwap(head):
    newHead = head
    # printLinkedList(head)
    if head.next is not None:
        newHead = head.next

    first, second = head, head.next
    while first and second:
        nextNode = second.next
        second.next = first
        first.next = nextNode.next if nextNode and nextNode.next else nextNode
        first = nextNode
        second = nextNode.next if nextNode else None
    # printLinkedList(newHead)
    return newHead
    
def printLinkedList(head):
    stack = []
    while head:
        stack.append(head.value)
        head = head.next
    print(stack)

# 2nd solution
# O(n) time | O(n) space
def nodeSwap(head):
    if head is None or head.next is None:
        return head
    nextNode = head.next
    head.next = nodeSwap(head.next.next)
    nextNode.next = head
    return nextNode

# 3rd solution
# O(n) time | O(1) space
def nodeSwap(head):
    tempNode = LinkedList(0)
    tempNode.next = head

    prevNode = tempNode
    while prevNode.next is not None and prevNode.next.next is not None:
        firstNode = prevNode.next
        secondNode = prevNode.next.next
        # prevNode -> firstNode -> secondNode -> x

        firstNode.next = secondNode.next
        secondNode.next = firstNode
        prevNode.next = secondNode
        # prevNode -> secondNode -> firstNode -> x

        prevNode = firstNode
    
    return tempNode.next