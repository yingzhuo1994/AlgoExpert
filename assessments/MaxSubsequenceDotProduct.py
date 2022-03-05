# 1st solution
def maxSubsequenceDotProduct(arrayOne, arrayTwo):
    minLength = min(len(arrayOne), len(arrayTwo))
    ans = float("-inf")
    for length in range(1, minLength + 1):
        ans = max(ans, getMaxProductAtLength(arrayOne, arrayTwo, length))
    return ans

def maxtrixDotProduct(arrayOne, arrayTwo):
    product = 0
    for i in range(len(arrayOne)):
        product += arrayOne[i] * arrayTwo[i]
    return product

def getMaxProductAtLength(arrayOne, arrayTwo, length):
    arrayOneWithLength = getSubarrayAtLength(arrayOne, length)
    arrayTwoWithLength = getSubarrayAtLength(arrayTwo, length)
    ans = float("-inf")
    for one in arrayOneWithLength:
        for two in arrayTwoWithLength:
            product = maxtrixDotProduct(one, two)
            ans = max(ans, product)
    return ans

def getSubarrayAtLength(array, length):
    if length == 1:
        return [[num] for num in array]
    stack = []
    for i in range(len(array) - length + 1):
        num = array[i]
        subArrays = getSubarrayAtLength(array[i+1:], length-1)
        for lst in subArrays:
            stack.append([num] + lst)
    return stack

# 2nd solution
# O(n * m) time | O(n * m) space 
# where n is the length of the first input array
# and m is the length of the second input array
def maxSubsequenceDotProduct(arrayOne, arrayTwo):
    maxDotProducts = initializeDotProducts(arrayOne, arrayTwo)
    for i in range(1, len(arrayOne) + 1):
        for j in range(1, len(arrayTwo) + 1):
            currentProduct = arrayOne[i - 1] * arrayTwo[j - 1]
            maxDotProducts[i][j] = max(
                currentProduct,
                maxDotProducts[i - 1][j - 1] + currentProduct,
                maxDotProducts[i - 1][j - 1],
                maxDotProducts[i - 1][j],
                maxDotProducts[i][j - 1],
            )
    return maxDotProducts[len(arrayOne)][len(arrayTwo)]

def initializeDotProducts(arrayOne, arrayTwo):
    dotProducts = [[float("-inf") for j in range(len(arrayTwo) + 1)] for i in range(len(arrayOne) + 1)]
    return dotProducts