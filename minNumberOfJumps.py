# 1st solution
# O(n^2) time | O(n) space
def minNumberOfJumps(array):
    table = [float('inf') for _ in array]
    table[0] = 0
    for i in range(len(array)):
        for j in range(1, array[i] + 1):
            if i + j < len(array):
                table[i + j] = min(table[i + j], table[i] + 1)
    return table[-1]

# 2nd solution
# O(n) time | O(n) space
def minNumberOfJumps(array):
    table = [float('inf') for _ in array]
    table[0] = 0
    maxDistance = 0
    for i in range(len(array)):
        if i + array[i] > maxDistance:
            j = maxDistance + 1
            maxDistance = i + array[i]
            while j <= maxDistance and j < len(array):
                table[j] = table[i] + 1
                j += 1
        if maxDistance >= len(array):
            break
    return table[-1]
