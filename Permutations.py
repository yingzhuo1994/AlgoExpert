# Upper Bound: O(n^2*n!) time | O(n*n!) space
# Roughly: O(n*n!) time | O(n*n!) space
def getPermutations(array):
    if len(array) == 1:
        return [array]
    
    lst = []
    for i, num in enumerate(array):
        lst.extend([[num] + k for k in getPermutations(array[:i] + array[i+1:])])
    return lst
