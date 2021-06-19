# O(n^2) time | O(n) space
def sortStack(stack):
    # Write your code here.
    if not stack:
        return stack
    lastNum = stack.pop()
    sortStack(stack)
    insertNum(stack, lastNum)
    return stack

def insertNum(stack, num):
    if not stack or num >= stack[-1]:
        stack.append(num)
    else:
        lastNum = stack.pop()
        insertNum(stack, num)
        insertNum(stack, lastNum)

