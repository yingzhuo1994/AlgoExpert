def firstDuplicateValue(array):
    # 1st solution
    # O(n) time | O(n) space
    # dic = {}
    # for elem in array:
    #     if elem in dic:
    #         return elem
    #     else:
    #         dic[elem] = 1
    # return -1

    # 2nd solution
    # O(n) time | O(n) space
    for i in range(len(array)):
        if array[i] in array[:i]:
            return array[i]
    return -1

    # 3rd solution
    # O(n) time | O(1) space
    for i in range(len(array)):
        index = abs(array[i]) - 1
        if array[index] < 0:
            return abs(array[i])
        else:
            array[index] *= -1
    return -1
