# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# 1st solution
# O(n) time | O(1) space
def reverseAlternatingKNodes(head, k):
    sentinel = LinkedList(0)
    p = sentinel
    needReverse = True
    node = head
    while node:
        if needReverse:
            newTail = node
            prev = None
            count = 0
            while node and count < k:
                nextNode = node.next
                node.next = prev
                prev = node
                node = nextNode
                count += 1
            p.next = prev
            p = newTail
            needReverse = False
        else:
            count = 0
            while node and count < k:
                p.next = node
                node = node.next
                p = p.next
                count += 1
            needReverse = True
    return sentinel.next
