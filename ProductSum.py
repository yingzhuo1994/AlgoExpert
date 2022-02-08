# O(n) time | O(d) space
# where n is the total number of elements in the array,
# including sub-subelements, and d is the greatest depth of "special" arrays in the array
def productSum(array, multiplier=1):
    ans = 0
    for element in array:
        if type(element) is list:
            ans += productSum(element, multiplier + 1)
        else:
            ans += element
    return ans * multiplier