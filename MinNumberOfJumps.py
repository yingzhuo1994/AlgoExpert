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

# 3rd solution
# O(n) time | O(1) space
def minNumberOfJumps(array):
    if len(array) == 1:
        return 0
    jumps = 0
    maxReach = array[0]
    steps = array[0]
    for i in range(1, len(array) - 1):
        maxReach = max(maxReach, i + array[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = maxReach - i
    return jumps + 1