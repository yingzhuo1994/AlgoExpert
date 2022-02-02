import heapq
# 1st solution
# O(n*log(k)) time | O(k) space
# where n is the nubmer of elements in the array
# and k is how far away elements are from their sorted position
def sortKSortedArray(array, k):
    if k > len(array):
        array.sort()
        return array
    stack = []
    for i in range(min(k, len(array))):
        heapq.heappush(stack, array[i])
    idx = k
    i = 0
    while stack:  
        if idx < len(array):
            heapq.heappush(stack, array[idx])
        idx += 1
        array[i] = heapq.heappop(stack)
        i += 1
    return array