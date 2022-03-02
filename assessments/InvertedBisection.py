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
