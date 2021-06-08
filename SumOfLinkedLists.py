# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(max(n, m)) time | O(max(n, m)) space 
# where n, m are the lengh of the first and the second Linked List separately
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    sentinel = LinkedList(0)
    currentNode = sentinel
    carry = 0

    nodeOne = linkedListOne
    nodeTwo = linkedListTwo

    while nodeOne or nodeTwo or carry > 0:
        valueOne = nodeOne.value if nodeOne else 0
        valueTwo = nodeTwo.value if nodeTwo else 0
        sumOfValues = valueOne + valueTwo + carry

        newValue = sumOfValues % 10
        newNode = LinkedList(newValue)
        currentNode.next = newNode
        currentNode = currentNode.next

        carry = sumOfValues // 10
        nodeOne = nodeOne.next if nodeOne else None
        nodeTwo = nodeTwo.next if nodeTwo else None
    
    return sentinel.next