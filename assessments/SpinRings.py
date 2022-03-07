# 1st solution
# O(n^2) time | O(1) space
def spinRings(array):
    n = len(array)
    for k in range(n // 2):
        rotate(array, k)
    return array

def rotate(array, k):
    start = k
    end = len(array) - k
    tmp = array[start][start]
    for j in range(start + 1, end):
        array[start][j], tmp = tmp, array[start][j]
    
    for i in range(start + 1, end):
        array[i][end-1], tmp = tmp, array[i][end-1]
    
    for j in reversed(range(start, end - 1)):
        array[end-1][j], tmp = tmp, array[end-1][j]
    
    for i in reversed(range(start, end - 1)):
        array[i][start], tmp = tmp, array[i][start]