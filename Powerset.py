# 1st solution
# O(n * 2^n) time | O(n * 2^n) space
def powerset(array):
    if not array:
        return [array]

    withoutNum = powerset(array[1:])
    withNum = [[array[0]] + k for k in withoutNum]
    return withoutNum + withNum

# 2nd iterative solution
# O(n * 2^n) time | O(n * 2^n) space
def powerset(array):
    subsets = [[]]
    for elem in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [elem])
    return subsets

# 3rd recursive solution
# O(n * 2^n) time | O(n * 2^n) space
def powerset(array, idx = None):
    if idx is None:
        idx = len(array) - 1
    if idx < 0:
        return [[]]
    elem = array[idx]
    # avoid using list slicing array[:idx-1]
    subsets = powerset(array, idx - 1)
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [elem])
    return subsets

# 4th solution
def powerset(array):
    lst = [[]]
	for num in array:
		lst += [k + [num] for k in lst]
	return lst
