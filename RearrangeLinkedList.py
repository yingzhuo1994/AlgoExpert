# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# 1st solution
# O(n) time | O(1) space
def rearrangeLinkedList(head, k):
    front = LinkedList(0)
    back = LinkedList(0)
    middle = LinkedList(0)
    p1, p2 = front, back
    p0 = middle
    while head:
        if head.value < k:
            p1.next = head
            head = head.next
            p1 = p1.next
            p1.next = None
        elif head.value > k:
            p2.next = head
            head = head.next
            p2 = p2.next
            p2.next = None
        else:
            p0.next = head
            head = head.next
            p0 = p0.next
            p0.next = None
    if middle.next is not None:
        p0.next = back.next
    else:
        middle.next = back.next
    if front.next is not None:
        p1.next = middle.next
    else:
        front.next = middle.next
    return front.next

# 2nd solution
# O(n) time | O(1) space
def rearrangeLinkedList(head, k):
    smallerListHead = None
    smallerListTail = None
    equalListHead = None
    equalListTail = None
    greaterListHead = None
    greaterListTail = None

    node = head
    while node is not None:
        if node.value < k:
            smallerListHead, smallerListTail = growLinkedList(smallerListHead, smallerListTail, node)
        elif node.value > k:
            greaterListHead, greaterListTail = growLinkedList(greaterListHead, greaterListTail, node)
        else:
            equalListHead, equalListTail = growLinkedList(equalListHead, equalListTail, node)
        
        prevNode = node
        node = node.next
        prevNode.next = None

    firstHead, firstTail = connectLinkedLists(smallerListHead, smallerListTail, equalListHead, equalListTail)
    finalHead, _ = connectLinkedLists(firstHead, firstTail, greaterListHead, greaterListTail)
    return finalHead

def growLinkedList(head, tail, node):
    newHead = head
    newTail = node

    if newHead is None:
        newHead = node
    if tail is not None:
        tail.next = node
    
    return (newHead, newTail)

def connectLinkedLists(headOne, tailOne, headTwo, tailTwo):
    newHead = headTwo if headOne is None else headOne
    newTail = tailOne if tailTwo is None else tailTwo

    if tailOne is not None:
        tailOne.next = headTwo
    
    return (newHead, newTail)