def findThreeLargestNumbers(array):
    lst = []
    for num in array:
        insertNum(lst, num)
    return lst

# 1st tedious solution
# def insertNum(lst, num):
#     print(lst)
#     if len(lst) == 0:
#         lst.append(num)
#     elif num <= lst[0]:
#         lst.insert(0, num)
#     elif num > lst[-1]:
#         lst.append(num)
#     elif num > lst[-2]:
#         lst.insert(-1, num)
#     elif num > lst[-3]:
#         lst.insert(-2, num)
#     if len(lst) > 3:
#         lst.pop(0)

# 2nd generalized solution
def insertNum(lst, num):
    # this could be use for N largest number
    N = 3
    if len(lst) == 0 or num > lst[-1]:
        lst.append(num)
    else:
        # should use binary search and deque
        for i in range(len(lst)):
            if num <= lst[i]:
                lst.insert(i, num)
                break
    if len(lst) > N:
        lst.pop(0)

# 3rd solution, Official
# O(n) time | O(1) space
def findThreeLargestNumbers(array):
    threeLargest = [None, None, None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest

def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)

def shiftAndUpdate(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1] 