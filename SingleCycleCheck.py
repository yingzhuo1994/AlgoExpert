def hasSingleCycle(array):
    # Write your code here.
    lst = []
    i = 0
    while i not in lst:
        lst.append(i)
        i = getIndex(array, i)
    return len(lst) == len(array) and  getIndex(array, lst[-1]) == lst[0]

def getIndex(array, k):
    index = k + array[k]
    if 0 <= index <= len(array) - 1:
        return index
    else:
        return index % len(array)
    

