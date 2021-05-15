# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# def findKthLargestValueInBst(tree, k):
#     # Write your code here.
#     dic = getAllValues(tree, [])
#     return dic[-k]
#
# def getAllValues(tree, dic = []):
#     if not tree:
#         return dic
#     if not dic:
#         dic.append(tree.value)
#     else:
#         if tree.value >= dic[-1]:
#             dic.append(tree.value)
#         else:
#             for i in range(len(dic)):
#                 if tree.value < dic[i]:
#                     dic.insert(i, tree.value)
#                     break
#     getAllValues(tree.left, dic)
#     getAllValues(tree.right, dic)
#     return dic

# def findKthLargestValueInBst(tree, k):
    # def helper(t):
    #     if not t:
    #         return []
    #     dic = [t.value]
    #     left = helper(t.left)
    #     right = helper(t.right)
    #     dic = left + dic + right
    #     return dic
    # dic = helper(tree)
    # return dic[-k]


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    def helper(t, dic = [0, -1]):
        if not t or dic[0] >= k:
            return
        helper(t.right, dic)
        if dic[0] < k:
            dic[0] += 1
            dic[1] = t.value
            helper(t.left, dic)
        return dic
    dic = helper(tree)
	print(dic)
    return dic[-1]
