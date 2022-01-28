# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# 1st solution
# O(n) time | O(1) space
def nodeSwap(head):
    newHead = head
    printLinkedList(head)
    if head.next is not None:
        newHead = head.next
    prev = None
    while head and head.next:
        first = head
        second = head.next
        nextNode = head.next.next
        second.next = first
        first.next = nextNode
        if prev is not None:
            prev.next = second
        prev = first
        head = nextNode
    printLinkedList(newHead)
    return newHead
    
def printLinkedList(head):
    stack = []
    while head:
        stack.append(head.value)
        head = head.next
    print(stack)