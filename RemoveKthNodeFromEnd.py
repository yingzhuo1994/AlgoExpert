# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) time
def removeKthNodeFromEnd(head, k):
    counter = 1
    first = head
    second = head
    while counter <= k:
        second = second.next
        counter += 1
    
    if not second:
        head.value = head.next.value
        head.next = head.next.next
        return 
    
    while second.next:
        second = second.next
        first = first.next
    first.next = first.next.next

    
