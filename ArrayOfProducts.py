# 1st solution
# O(n^2) time | O(n) space
# where n is the length of the input array
def arrayOfProducts(array):
    products = [1 for _ in array]

    for i in range(len(array)):
        runningProduct = 1
        for j in range(len(array)):
            if i != j:
                runningProduct *= array[j]
        products[i] = runningProduct
    
    return products

# 2nd solution
# O(n) time | O(n) space
# where n is the length of the input array
def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]
    leftProducts = [1 for _ in range(len(array))]
    rightProducts = [1 for _ in range(len(array))]

    leftRunningProduct = 1
    for i in range(len(array)):
        leftProducts[i] = leftRunningProduct
        leftRunningProduct *= array[i]
    
    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        rightProducts[i] = rightRunningProduct
        rightRunningProduct *= array[i]
    
    for i in range(len(array)):
        products[i] = leftProducts[i] * rightProducts[i]
    
    return products


# 3rd solution
# O(n) time | O(n) space
# where n is the length of the input array
def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]

    leftRunningProduct = 1
    for i in range(len(array)):
        products[i] = leftRunningProduct
        leftRunningProduct *= array[i]
    
    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= rightRunningProduct
        rightRunningProduct *= array[i]
    
    return products