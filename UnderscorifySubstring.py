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

# 2nd solution
# O(n + m) time | O(n) space
# where n is the length of the main string and m is the length of the substring
def underscorifySubstring(string, substring):
    locations = collapse(getLocations(string, substring))
    return underscorify(string, locations)

def getLocations(string, substring):
    locations = []
    startIdx = 0
    while startIdx < len(string):
        nextIdx = string.find(substring, startIdx)
        if nextIdx != -1:
            locations.append([nextIdx, nextIdx + len(substring)])
            startIdx = nextIdx + 1
        else:
            break
    return locations

def collapse(locations):
    if not len(locations):
        return locations
    newLocations = [locations[0]]
    previous = newLocations[0]
    for i in range(1, len(locations)):
        current = locations[i]
        if current[0] <= previous[1]:
            previous[1] = current[1]
        else:
            newLocations.append(current)
            previous = current
    return newLocations

def underscorify(string, locations):
    locationsIdx = 0
    stringIdx = 0
    inBetweenUnderscors = False
    finalChars = []
    i = 0
    while stringIdx < len(string) and locationsIdx < len(locations):
        if stringIdx == locations[locationsIdx][i]:
            finalChars.append("_")
            inBetweenUnderscors = not inBetweenUnderscors
            if not inBetweenUnderscors:
                locationsIdx += 1
            i = 0 if i == 1 else 1
        finalChars.append(string[stringIdx])
        stringIdx += 1
    if locationsIdx < len(locations):
        finalChars.append("_")
    elif stringIdx < len(string):
        finalChars.append(string[stringIdx:])
    return "".join(finalChars)
