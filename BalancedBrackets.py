# O(n) time | O(n) space
def balancedBrackets(string):
    dic = {'(':')',
           '[':']',
           '{':'}'
          }
    stack = []
    for ch in string:
        if ch in dic:
            stack.append(ch)
        elif ch in ')]}':
            if not stack:
                return False
            lastParen = stack.pop()
            if dic[lastParen] != ch:
                return False
    return not stack

# O(n) time | O(n) space
def balancedBrackets(string):
    openingBrackets = "([{"
    closingBrackets = ")]}"
    matchingBrackets = {")": "(", "]": "[", "}": "{"}
    stack = []
    for char in string:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if len(stack) == 0:
                return False
            if stack[-1] == matchingBrackets[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0