# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    size = 0
    p = head
    while p:
        p = p.next
        size += 1
    if k == size:
        if head.next:
            head.value = head.next.value
            head.next = head.next.next
        else:
            head = head.next
    else:
        p = head
        while size - k - 1 > 0:
            p = p.next
            k += 1
        p.next = p.next.next
    
