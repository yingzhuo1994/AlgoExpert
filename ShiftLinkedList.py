# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# 1st solution
# O(n) time | O(1) space
def shiftLinkedList(head, k):
    if k == 0:
        return head
    length = 0
    prev = None
    p = head
    while p:
        length += 1
        prev = p
        p = p.next
    end = prev

    k = k % length
    if k > 0:
        steps = length - k
    elif k < 0:
        steps = length + k
    else:
        return head
    
    prev = None
    p = head
    while steps > 0:
        prev = p
        p = p.next
        steps -= 1
    
    if prev == None:
        return head
    else:
        end.next = head
        prev.next = None
    
    return p

# 2nd solution, official
# O(n) time | O(1) space
def shiftLinkedList(head, k):
    listLength = 1
    listTail = head
    while listTail.next is not None:
        listTail = listTail.next
        listLength += 1
    
    offset = abs(k) % listLength
    if offset == 0:
        return head
    
    newTailPosition = listLength - offset if k > 0 else offset
    newTail = head
    for i in range(1, newTailPosition):
        newTail = newTail.next
    
    newHead = newTail.next
    newTail.next = None
    listTail.next = head
    return newHead