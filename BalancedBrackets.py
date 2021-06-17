# O(n) time | O(n) space
def balancedBrackets(string):
    # Write your code here.
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