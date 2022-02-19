# O(n^2) time | O(n) space
def sortStack(stack):
    if len(stack) == 0:
        return stack

    top = stack.pop()
    sortStack(stack)
    insertInSortedOrder(stack, top)
    return stack

def insertInSortedOrder(stack, value):
    if not stack or value >= stack[-1]:
        stack.append(value)
    else:
        top = stack.pop()
        insertInSortedOrder(stack, value)
        stack.append(top)