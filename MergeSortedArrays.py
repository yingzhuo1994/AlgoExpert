# 1st solution
# O(n) time | O(n) space
def mergeSortedArrays(arrays):
    n = len(arrays)
    interval = 1
    while interval < n:
        for i in range(0, n, interval * 2):
            arrays[i] = mergeTwoArrays(arrays, i, i + interval)
        interval *= 2
    return arrays[0]

def mergeTwoArrays(arrays, a, b):
    if b >= len(arrays):
        return arrays[a]
    one = arrays[a]
    two = arrays[b]
    if not one or not two:
        return one or two
    ans = []
    i, j = 0, 0
    while i < len(one) and j < len(two):
        if one[i] < two[j]:
            ans.append(one[i])
            i += 1
        else:
            ans.append(two[j])
            j += 1
    ans.extend(one[i:] or two[j:])
    return ans