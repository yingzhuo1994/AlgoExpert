def productSum(array):
    # Write your code here.

    def helper(array, depth = 1):
        result = 0
        for elem in array:
            if isinstance(elem, int):
                result += elem
            else:
                result += helper(elem, depth + 1)
        return depth * result
    return helper(array, 1)
