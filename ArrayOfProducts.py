def arrayOfProducts(array):
    # Write your code here.
    # lst = []
    # for i in range(len(array)):
    #     products = 1
    #     for j in range(len(array)):
    #         if j != i:
    #             products *= array[j]
    #     lst.append(products)
    # return lst

    # 2nd solution
    # lst = []
    # left, right = 1, 1
    # for i in range(len(array)):
    #     lst.append(left)
    #     left *= array[i]
    # for i in reversed(range(len(array))):
    #     lst[i] *= right
    #     right *= array[i]
    # return lst

    # 3rd solution
    n = len(array)
    lst = [1 for _ in range(n)]
    left, right = 1, 1
    for i in range(len(array)):
        lst[i] *= left
        lst[n-1-i] *= right
        left *= array[i]
        right *= array[n-1-i]
    return lst
