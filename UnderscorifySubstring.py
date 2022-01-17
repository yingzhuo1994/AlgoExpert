# 1st solution
# O(n) time | O(n) space
def underscorifySubstring(string, substring):
    stack = []
    for i in range(len(string)):
        r = findRange(string, substring, i)
        if r is not None:
            stack.append(r)
    if len(stack) == 0:
        return string
    mergeStack = [stack[0]]
    for i in range(1, len(stack)):
        if stack[i][0] <= mergeStack[-1][1] + 1:
            mergeStack[-1][1] = stack[i][1]
        else:
            mergeStack.append(stack[i])
    idxSet = set()
    for pair in mergeStack:
        idxSet.add(pair[0])
        idxSet.add(pair[1] + 1)
    ans = []
    k = 0
    for i in range(len(string)):
        if i in idxSet:
            ans.append("_")
        ans.append(string[i])
    if len(string) in idxSet:
        ans.append("_")
    return "".join(ans)

def findRange(string, substring, idx):
    for i in range(len(substring)):
        if idx + i >= len(string) or string[idx + i] != substring[i]:
            return None
    return [idx, idx + len(substring) - 1]

