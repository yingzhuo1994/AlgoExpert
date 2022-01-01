# 1st solution
def interweavingStrings(one, two, three):
    def check(i, j, k):
        if k == len(three):
            return i == len(one) and j == len(two)
        addOne = False
        addTwo = False
        if i < len(one) and one[i] == three[k]:
            addOne = check(i + 1, j, k + 1)
        if j < len(two) and two[j] == three[k]:
            addTwo = check(i, j + 1, k + 1)
        return addOne or addTwo
    
    return check(0, 0, 0)