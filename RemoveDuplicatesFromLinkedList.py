# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    p = linkedList
    while p.next:
        if p.value == p.next.value:
            p.next = p.next.next
        else:
            p = p.next
    return linkedList
