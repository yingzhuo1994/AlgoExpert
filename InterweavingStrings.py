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

# 2nd solution
# O(2^(n + m)) time | O(n + m) space - where n is the length
# of the first string and m is the length of the second string
def interweavingStrings(one, two, three):
    if len(three) != len(one) + len(two):
        return False
    
    return areInterwoven(one, two, three, 0, 0)

def areInterwoven(one, two, three, i, j):
    k = i + j
    if k == len(three):
        return True
    
    if i < len(one) and one[i] == three[k]:
        if areInterwoven(one, two, three, i + 1, j):
            return True
    
    if j < len(two) and two[j] == three[k]:
        return areInterwoven(one, two, three, i, j + 1)
    
    return False