def numberOfBinaryTreeTopologies(n):
    dic = {0: 1, 1: 1}
    def createBinaryTree(k, dic):
        if k not in dic:
            count = 0
            for i in range(1, k + 1):
                count += createBinaryTree(i - 1, dic) * createBinaryTree(k  - i, dic)
            dic[k] = count
        return dic[k]
    return createBinaryTree(n, dic)