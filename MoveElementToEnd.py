def moveElementToEnd(array, toMove):
    # Write your code here.
    # p1 = 0
    # p2 = len(array) - 1
    # while p1 < p2:
    #     if array[p2] == toMove:
    #         p2 -= 1
    #     elif array[p1] == toMove:
    #         array[p1], array[p2] = array[p2], array[p1]
    #         p1 += 1
    #         p2 -= 1
    #     else:
    #         p1 += 1
    # return array
    p1, p2 = 0, len(array) - 1
    for i in range(len(array)):
        if array[i] != toMove:
            p1 = i
        else:
            if i == 0 or array[i -1] != toMove:
                p2 = i
        if p2 < p1:
            array[p1], array[p2] = array[p2], array[p1]
            p1 = 0
            p2 += 1
    return array

def moveElementToEnd(array, toMove):
    # Solve this in original order
    pMove = len(array)
    for i in range(len(array)):
        if array[i] == toMove and pMove == len(array):
            pMove = i
        if array[i] != toMove and pMove < i:
            swap(i, pMove, array)
            pMove += 1
    return array

def swap(i, j , array):
    array[i], array[j] = array[j], array[i]
