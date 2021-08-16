def minNumberOfJumps(array):
    table = [float('inf') for _ in array]
    table[0] = 0
    for i in range(len(array)):
        for j in range(1, array[i] + 1):
            if i + j < len(array):
                table[i + j] = min(table[i + j], table[i] + 1)
    return table[-1]