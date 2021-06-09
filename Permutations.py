def getPermutations(array):
    # Write your code here.
    if not array:
        return []

    if len(array) == 1:
        return [array]
    
    lst = []
    for i, num in enumerate(array):
        lst.extend([[num] + k for k in getPermutations(array[:i] + array[i+1:])])
    return lst
