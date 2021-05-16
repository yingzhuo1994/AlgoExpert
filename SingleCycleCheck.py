def hasSingleCycle(array):
    # Write your code here.
    # 1st solution
    # O(n) time | O(n) space
    lst = []
    i = 0
    while i not in lst:
        lst.append(i)
        i = getIndex(array, i)
    return len(lst) == len(array) and  getIndex(array, lst[-1]) == lst[0]

    # 2nd solution
    # O(n) time | O(1) space
    numElemVisited = 0
    i = 0
    while numElemVisited < len(array):
        if numElemVisited > 0 and i == 0:
            return False
        numElemVisited += 1
        i = getIndex(array, i)
    return i == 0   

def getIndex(array, k):
    index = k + array[k]
    if 0 <= index <= len(array) - 1:
        return index
    else:
        return index % len(array)
    

