# 1st solution
# O(n) time | O(n) space
def hasSingleCycle(array):
    visited = []
    i = 0
    while i not in visited:
        visited.append(i)
        i = getNextIdx(array, i)
    return len(visited) == len(array) and  i == 0

# 2nd solution
# O(n) time | O(1) space
def hasSingleCycle(array):
    numElementsVisited = 0
    currentIdx = 0
    while numElementsVisited < len(array):
        if numElementsVisited > 0 and currentIdx == 0:
            return False
        numElementsVisited += 1
        currentIdx = getNextIdx(array, currentIdx)
    return currentIdx == 0   

def getNextIdx(array, currentIdx):
    jump = array[currentIdx]
    nextIdx = (currentIdx + jump) % len(array)
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)

# 3rd solution, simplified solution
# O(n) time | O(1) space
def hasSingleCycle(array):
    numElementsVisited = 0
    currentIdx = 0
    while numElementsVisited < len(array):
        numElementsVisited += 1
        currentIdx = getNextIdx(array, currentIdx)
        if currentIdx == 0:
            break
    return currentIdx == 0 and numElementsVisited == len(array)   

def getNextIdx(array, currentIdx):
    jump = array[currentIdx]
    nextIdx = (currentIdx + jump) % len(array)
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)