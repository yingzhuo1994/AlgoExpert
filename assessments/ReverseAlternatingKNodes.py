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

# 2nd solution
# O(n) time | O(1) space
# where n is the number of nodes in the Linked List
def reverseAlternatingKNodes(head, k):
    finalHead = None
    
    isGroupToReverse = True
    runningK = 1

    previousGroupTail = None
    currentGroupHead = head
    currentNode = head

    while currentNode is not None:
        shouldReverse = isGroupToReverse and (runningK == k or currentNode.next is None)

        if not shouldReverse:
            if runningK == k:
                runningK = 1
                isGroupToReverse = True

                previousGroupTail = currentNode
                currentGroupHead = currentNode.next
            else:
                runningK += 1
            
            currentNode = currentNode.next
            continue

        runningK = 1
        isGroupToReverse = False
        
        nextNode = currentNode.next
        currentNode.next = None
        reversedGroupHead = reverseLinkedList(currentGroupHead)
        reversedGroupTail = currentGroupHead
        reversedGroupTail.next = nextNode

        if previousGroupTail is None:
            finalHead = reversedGroupHead
        else:
            previousGroupTail.next = reversedGroupHead
        
        currentNode = nextNode
        currentGroupHead = nextNode
        previousGroupTail = reversedGroupTail
    
    return finalHead

def reverseLinkedList(head):
    previousNode, currentNode = None, head
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    return previousNode

# 3rd solution
# O(n) time | O(1) space
# where n is the number of nodes in the Linked List
def reverseAlternatingKNodes(head, k):
    finalHead = None
    
    previousNode = None
    currentNode = head
    while currentNode is not None:
        reversedGroupHead, nextNode = reverseKNodes(currentNode, k)
        # The `currentNode` is now the tail of the reversed group,
        # so we make it point to the `nextNode`
        currentNode.next = nextNode
        currentNode = nextNode

        if previousNode is None:
            finalHead = reversedGroupHead
        else:
            previousNode.next = reversedGroupHead
        
        skippedNodesCount = 0
        while currentNode is not None and skippedNodesCount < k:
            previousNode = currentNode
            currentNode = currentNode.next

            skippedNodesCount += 1
    
    return finalHead

def reverseKNodes(head, k):
    reversedNodesCount = 0
    previousNode, currentNode = None, head
    while currentNode is not None and reversedNodesCount < k:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode

        reversedNodesCount += 1
    
    return (previousNode, currentNode)