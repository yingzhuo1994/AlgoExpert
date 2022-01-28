# 1st solution
# O(n^2) time | O(n) space
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

# 2nd solution
# Upper Bound: O((n*(2n)!)/(n!(n+1)!)) time | O(n) space
def numberOfBinaryTreeTopologies(n):
    if n == 0:
        return 1
    numberOfTrees = 0
    for leftTreeSize in range(n):
        rightTreeSize = n - 1 - leftTreeSize
        numberOfLeftTrees = numberOfBinaryTreeTopologies(leftTreeSize)
        numberOfRightTrees = numberOfBinaryTreeTopologies(rightTreeSize)
        numberOfTrees += numberOfLeftTrees * numberOfRightTrees
    return numberOfTrees

# 3rd solution
# O(n^2) time | O(n) space
def numberOfBinaryTreeTopologies(n, cache={0:1}):
    if n in cache:
        return cache[n]
    numberOfTrees = 0
    for leftTreeSize in range(n):
        rightTreeSize = n - 1 - leftTreeSize
        numberOfLeftTrees = numberOfBinaryTreeTopologies(leftTreeSize, cache)
        numberOfRightTrees = numberOfBinaryTreeTopologies(rightTreeSize, cache)
        numberOfTrees += numberOfLeftTrees * numberOfRightTrees
    cache[n] = numberOfTrees
    return numberOfTrees

# 4th solution
# O(n^2) time | O(n) space
def numberOfBinaryTreeTopologies(n):
    cache = [1]
    for m in range(1, n + 1):
        numberOfTrees = 0
        for leftTreeSize in range(m):
            rightTreeSize = m - 1 - leftTreeSize
            numberOfLeftTrees = cache[leftTreeSize]
            numberOfRightTrees = cache[rightTreeSize]
            numberOfTrees += numberOfLeftTrees * numberOfRightTrees
        cache.append(numberOfTrees)
    return cache[n]