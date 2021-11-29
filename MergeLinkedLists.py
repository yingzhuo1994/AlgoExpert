# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# 1st solution
# O(m + n) time | O(1) space
def mergeLinkedLists(headOne, headTwo):
    sentinel = LinkedList(0)
    p = sentinel
    while headOne and headTwo:
        if headOne.value <= headTwo.value:
            p.next = headOne
            headOne = headOne.next
        else:
            p.next = headTwo
            headTwo = headTwo.next
        p = p.next
    p.next = headOne or headTwo
    return sentinel.next