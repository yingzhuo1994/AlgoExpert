def findThreeLargestNumbers(array):
    # Write your code here.
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
		for i in range(len(lst)):
			if num <= lst[i]:
				lst.insert(i, num)
				break
    if len(lst) > N:
        lst.pop(0)
